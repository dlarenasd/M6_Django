"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import index, about, welcome, base, contacto, exito, registro, masterflan


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='indice'),
    path('acerca/', about, name='acerca'),
    path('bienvenido/', welcome, name='bienvenido'),
    path('base', base, name='base'),
    #path('login/', login, name='login'),
    path('contacto/', contacto, name='contacto'),
    path('contacto/exito/', exito, name='exito'),
    path('registro/', registro, name='registro'),
    path('masterflan/', masterflan, name='masterflan'),
    path('accounts/', include('django.contrib.auth.urls')),

]

