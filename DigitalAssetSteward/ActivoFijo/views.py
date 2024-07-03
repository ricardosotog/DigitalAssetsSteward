from django.shortcuts import render, redirect
from .forms import LoginForm, ActivoForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def  home(request):
    return render(request,'ActivoFijo/home.html')
def  activo(request):
    return render(request,'ActivoFijo/activo.html')
def  software(request):
    return render(request,'ActivoFijo/software.html')
def  consumible(request):
    return render(request,'ActivoFijo/consumible.html')
def  hardware(request):
    return render(request,'ActivoFijo/hardware.html')
def  telefonia(request):
    return render(request,'ActivoFijo/telefonia.html')
def  plantelefono(request):
    return render(request,'ActivoFijo/plantelefono.html')

def Login(request):
    form =LoginForm()
    if request.method =="POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username =request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate (request, username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("home")
    return render(request, 'ActivoFijo/login.html',{'form':form})

def Add_Activo(request):
    #submitted = False
    #if request.method =="POST":
    form = ActivoForm
    return render(request, 'ActivoFijo/activo.html',{'form':form})

