from django.urls import path
from . import views as v
urlpatterns = [
    path('create_project/', v.create_project),
    path('edit_project/', v.edit_project),
    path('say_about_me/', v.say_about_me),
    path('search/', v.search),
]
