""" Platzigram middleware catalog. """

# Django
from django.shortcuts import redirect
from django.urls import reverse

# Models 

# Este middleware que cuando no tengamos un perfil listo no iba 
# a redireccionar a update profile.

class ProfileCompletionMiddleware:
    """ Profile completion middleware.
    
    Ensure every user that is interecting with the platform 
    have their profile picture and biography 
    """
    def __init__(self, get_response):
        """ Middleware initialization. """
        self.get_response = get_response
        
        # siemppre analizar que tiene el objeto profile
        # reverse > apartir de un nombre traer la url
    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.bigoraphy:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response
        
    