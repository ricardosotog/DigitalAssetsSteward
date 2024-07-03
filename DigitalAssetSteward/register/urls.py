from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"), 
    #path('logout/',logout_then_login, name='logout')
]