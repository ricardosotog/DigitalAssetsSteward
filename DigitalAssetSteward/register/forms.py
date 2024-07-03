from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


class RegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1=forms.PasswordInput
    password2=forms.PasswordInput
    class Meta:
        model =User
        fields = ["username","email","password1","password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput