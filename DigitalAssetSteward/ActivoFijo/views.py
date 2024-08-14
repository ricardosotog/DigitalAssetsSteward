from django.shortcuts import render, redirect
from .forms import LoginForm, ActivoForm, SearchForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def  home(request):
    return render(request,'ActivoFijo/home.html')
@login_required
def  activo(request):
    return render(request,'ActivoFijo/activo.html')
@login_required
def  software(request):
    return render(request,'ActivoFijo/software.html')
@login_required
def  consumible(request):
    return render(request,'ActivoFijo/consumible.html')
@login_required
def  hardware(request):
    return render(request,'ActivoFijo/hardware.html')
@login_required
def  telefonia(request):
    return render(request,'ActivoFijo/telefonia.html')
@login_required
def asignaciones(request):
    return render(request,'ActivoFijo/asignaciones.html')

def logout(request):
    auth.logout(request)
    return redirect("ActivoFijo/")


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
                return redirect("/home")
    return render(request, 'ActivoFijo/login.html',{'form':form})

def Add_Activo(request):
    if request.POST:
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save
        return render(request, 'ActivoFijo/home.html',{'form':ActivoForm})
def SerchActivo(request):
    form = SearchForm
    return render(request, 'ActivoFijo/asignaciones.html',{'form':form})

