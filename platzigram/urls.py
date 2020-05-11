"""platzigram URL Configuration"""

from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views

#llamando las vistas
urlpatterns = [

    #local views
    path('hello-word/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

     #New views
    path('posts/', posts_views.list_posts),




]
