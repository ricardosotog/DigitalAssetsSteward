from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Activos
from django.forms import ModelForm

    
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput

class ActivoForm(ModelForm):
    class Meta:
       model = Activos
       fields = ('kace','categoria','usuario_asignado','usuario_anterior','NoOrdenCompra','NoResponsiva','Sucursal','NoSerie','MarcaEquipo', 'ModeloEquipo','RAM','Almacenamiento')
       labels = {
            'kace':'',
            'categoria':'',
            'usuario_asignado':'',
            'usuario_anterior':'',
            'NoOrdenCompra':'',
            'NoResponsiva':'',
            'Sucursal':'',
            'NoSerie':'',
            'MarcaEquipo':'',
            'ModeloEquipo':'',
            'RAM':'',
            'Almacenamiento':'',
       }
       widgets = {
           'kace': forms.TextInput(attrs={'class' :'form-control','placeholder':'Ticket KACE'}),
           'categoria': forms.TextInput(attrs={'class' :'form-control','placeholder':'Categoria'}),
           'usuario_asignado': forms.TextInput(attrs={'class' :'form-control','placeholder':'Usuario Asignado'}),
            'usuario_anterior': forms.TextInput(attrs={'class' :'form-control','placeholder':'Usuario Anterior'}),
            'NoOrdenCompra':forms.TextInput(attrs={'class' :'form-control','placeholder':'No. Orden de Compra'}),
            'NoResponsiva':forms.TextInput(attrs={'class' :'form-control','placeholder':'No. Responsiva'}),
            'Sucursal':forms.TextInput(attrs={'class' :'form-control','placeholder':'Sucursal'}),
            'NoSerie':forms.TextInput(attrs={'class' :'form-control','placeholder':'No. Serial'}),
            'MarcaEquipo':forms.TextInput(attrs={'class' :'form-control','placeholder':'Marca del Equipo'}),
            'ModeloEquipo':forms.TextInput(attrs={'class' :'form-control','placeholder':'Modelo del Equipo'}),
            'RAM':forms.TextInput(attrs={'class' :'form-control','placeholder':'Memoria RAM'}),
       }
class SearchForm(ModelForm):
    class Meta:
       model = Activos
       fields = ('kace','Category','WorkSpace','NoSerial')
       labels = {
            'kace':'',
            'Category':'',
            'WorkSpace':'',
            'SerialNumber':'',
            }
       widgets = {
           'kace': forms.TextInput(attrs={'class' :'form-control','placeholder':'Ticket KACE'}),
           'categoria': forms.TextInput(attrs={'class' :'form-control','placeholder':'Categoria'}),
           'WorkSpace': forms.TextInput(attrs={'class' :'form-control','placeholder':'Usuario Asignado'}),
           'SerialNumber' : forms.TextInput(attrs={'class' :'form-control','placeholder':'Usuario Asignado'}),
       }
       