from django.shortcuts import render, redirect
from .models import Usuario
from .forms import ProveedorForm, SignUp




# Create your views here.

def bienvenida(request):
    return render(request, 'home/index.html', {
        } )

def mostrarUsuario(request):
    lista_usuario = Usuario.objects.all()
    return render(request, 'home/mostrar_usuario.html', {
        'lista_usuario' : lista_usuario
    })

def ingresarPosibleProveedor(request):
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home:bienvenida')
    return render (request, 'home/proveedorPostulante.html',{'formulario' : ProveedorForm()})

def signUp(request):
    if request.method == 'POST':
        formulario_post = SignUp(request.POST)
        if formulario_post.is_valid():
            formulario_post.save()
            return redirect ('home:bienvenida')
    return render(request, 'home/signUp.html',{
        'form' : SignUp()
    })