""" User admin classes."""

#Django
from django.contrib import admin

#Models
from users.models import Profile

# Register your models here.
# Agreganddo el Profile al admin de Django
#admin.site.register(Profile)
@admin.register(Profile)
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
    
    
    

    
    

