from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.Login, name='login'),
    path('', views.Login, name='login'),
    path('home/',views.home, name='home'),
    path('activo/',views.Add_Activo, name='activo'),
    path('software/',views.software, name='software'),
    path('consumible/',views.consumible, name='consumible'),
    path('hardware/',views.hardware, name='hardware'),
    path('telefonia/',views.telefonia, name='telefonia'),
    path('plantelefono/',views.plantelefono, name='plantelefono'),
]
#Hola! me puedes ayudar en regresar mi telefono? se dara compensacion a cambio vivo en calle rio tepalcatepec 506. o tambien me puedes marcar al:33 1738 2054