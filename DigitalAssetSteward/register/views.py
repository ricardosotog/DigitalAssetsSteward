from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import auth
# Create your views here.

def register(response):
    if response.method == "POST":
        form= RegisterForm(response.POST)
        if form.is_valid():
           print("Añadido")
           form.save
         #return redirect("templates/ActivoFijo/home.html")
        else:
         form= RegisterForm()
        return render(response, "register/register.html",{"form":form})


def log (request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
    return render(request, 'register/login.html', {'form':form})
    

def logout(reponse):
   return render