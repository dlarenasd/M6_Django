from django.shortcuts import render, redirect
from .models import Flan, ContactForm, FotoCarrusel
from .forms import ContactDataForm, ContactDataModelForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    context = {
        'flanes': flanes,
        'flanes_privados' : flanes_privados,
        'flanes_publicos': flanes_publicos
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes = Flan.objects.all()
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    
    context = {
        'flanes': flanes,
        'flanes_privados' : flanes_privados,
        'flanes_publicos': flanes_publicos
    }
    return render(request, 'welcome.html', context)

def base(request):
    return render(request, 'base.html')
""" 
def login(request):
    #post ->capturar datos desde el html
    if request.method == "POST":
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            email = (request.POST["email"])
            password = (request.POST["password"])
        #crear un objeto y asignar los valores
        #crear el registro en la base de datos
            #objeto.save()
        #uso de sesiones
        return HttpResponseRedirect('bienvenido/')
"""
def contacto(request):
    if request.method == "POST":
        formulario = ContactDataModelForm(request.POST)
        if formulario.is_valid():
            contact_form = ContactForm.objects.create(**formulario.cleaned_data)
            
            return HttpResponseRedirect('exito/')
            
    else:
        formulario = ContactDataModelForm()
    return render(request, 'contacto.html', {'formulario': formulario})

def exito(request):
    return render(request, 'exito.html')

            
def registro(request):
    if request.method == "POST":
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            username = (request.POST["username"])
            email = (request.POST["email"])
            password = (request.POST["password"])
        
            user = User.objects.create_user(username, email, password)
        
            user.first_name = (request.POST["first_name"])
            user.last_name = (request.POST["last_name"])
            
            user.save()#inserta o actualiza
            return redirect('login')
    else: 
        formulario = RegisterForm()
    return render(request, 'registro.html', {'formulario': formulario})

@login_required
def masterflan(request):
    fotos_carrusel = FotoCarrusel.objects.all()
    
    context = {
        'fotos_carrusel' : fotos_carrusel
    }
    return render(request, 'masterflan.html', context)

