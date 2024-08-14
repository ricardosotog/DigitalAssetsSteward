from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.Login, name='login'),
    path('ActivoFijo/', views.Login, name=''),
    path('home/',views.home, name='home'),
    path('activo/',views.Add_Activo, name='activo'),
    path('software/',views.software, name='software'),
    path('consumible/',views.consumible, name='consumible'),
    path('hardware/',views.hardware, name='hardware'),
    path('telefonia/',views.telefonia, name='telefonia'),
    path('asignaciones/',views.asignaciones,name='asignaciones'),
]
