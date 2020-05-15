"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

def update_profile(request):
    """ Update a user's profile view. """
    
    return render(request, 'users/update_profile.html')

    
    

def login_view(request):
    """Login view."""
    
    #devolviendo el usuario y contraseña
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #redirigiendo al feed
        if user:
            login(request, user)
            return redirect('feed')
        #error por usuario o contraseña invalida
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
        
    #retornando la url definida en url.py
    return render(request, 'users/login.html')


# Metodo de creacion de cuenta
def signup_view(request):
    """ Sig nup View. """
    
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        
        #validacion del registro del usuario
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})
        
        #creando el usuario
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'username is ready in user'})
            
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        #creando una instancia del modelo Profile
        profile = Profile(user=user)
        profile.save()
        
        return redirect('login')
        
    #import pdb; pdb.set_trace()
    return render (request, 'users/signup.html')
    

#para cuando quiera hacer logout de una sesion enexistente.
@login_required
def logout_view(request):
    """ Logout a user. """
    
    logout(request)
    return redirect('login')
    
    
