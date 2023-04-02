from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('createUser/', views.CreateUser, name= "CreateUser"),
    path('profile/', views.ProfilePage, name= 'ProfilePage')
]
