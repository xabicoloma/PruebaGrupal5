from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Proveedor, Usuario

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa','nombre_solicitante','email','telefono','rubro_proveedor','direccion','comentario']
        labels = {'Nombre empresa':'nombre_empresa',
                'Nombre solicitante' : 'nombre_solicitante',
                'Correo' : 'email',
                'Telefono de contacto' :'telefono',
                'Rubro de proveedor' :'rubro_proveedor',
                'Dirección' : 'direccion',
                'Comentario' : 'comentario'
                }
        
class SignUp(UserCreationForm):
    class Meta:
        model= Usuario
        fields = ['nombre', 'apellido', 'rut', 'email', 'telefono']
        labels = {
            'Nombres' : 'nombre',
            'Apellidos' : 'apellido',
            'Rut' : 'rut',
            'Correo electrónico': 'email',
            'Telefono de contacto' : 'telefono',
        }