""" User admin classes."""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
# Agreganddo el Profile al admin de Django
#admin.site.register(Profile)
@admin.register(Profile)   # = decorador para registrarlo.
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin."""
    
    # listar items
    list_display = ('pk','user','phone_number','website','picture')

    #a al dar click lleve al detalle(link)
    list_display_links = ('pk','user')

    #editar desde el administrador web(editable)
    list_editable = ('phone_number','website','picture')

    #BUSCAR en Profile(recibe los campos por los que se quieren buscar,
    #"user no es un campo, es una relacion") de user vamos a usar
    search_fields = ('user__email',
                     'user__username',
                     'user__first_name',
                     'user__last_name',
                     'phone_number'
    )
    #listar filtros en el web administrador de Django
    list_filter = ('created',
                   'modified',
                   'user__is_active',
                   'user__is_staff'
                   
    )
    #listar de los detalles de perfiles
    #añadiendo las categorias al change profile
    fieldsets = (
        ('profile', {
            'fields':(('user','picture'),), # de esta manera agrupamos en una sola fila.Tupla dentro de tupla
        }),
        
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('bigoraphy')
            )
        }),
        
        ('Metadata', {
            'fields':(('created','modified'),),
        })
    )
    
    #agregando la fecha de creacion y modificacion.
    readonly_fields = ('created','modified')
    
#agregando el Profile al User
class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users. """
    
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
    
class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin. """
    
    inlines = (ProfileInline,)
    #mostrando en el web admin estos items
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    
#registrando el admin  
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

    
    
    
    
    

        
        