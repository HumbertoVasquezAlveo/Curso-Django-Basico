""" Post Model """
#Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post Model. """
    
    # El usuario es la llave foranea.(|cada que se borre el usuario del post, lo hara en cascada
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # el User viene del modelo de User que viene de django
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) # escribviendo el nombre de la App > 'users' > despues nombre del modelo
    
    title = models.CharField(max_length=255)
    photo  = models.ImageField(upload_to='posts/photos')
    
    
    
    #agregando metadada(cuando se crea y cuando se modfica)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    #definir metodo string
    def __str__(self):
        """ Return title and username. """
        return '{} by @{}'.format(self.title, self.user.username)




