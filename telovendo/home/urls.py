from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('mostrarUsuario/', views.mostrarUsuario, name='mostrarUsuario'),
    path('contactanosProveedor/', views.ingresarPosibleProveedor, name='contactanosProveedor'),
    path('signUp/', views.signUp, name='signUp')
]