from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activos(models.Model):
    kace = models.IntegerField('TicketKace',blank=True, null=True)
    categoria = models.CharField(max_length=20)
    usuario_asignado = models.CharField(max_length=20)
    usuario_anterior = models.CharField(max_length=255)
    NoOrdenCompra = models.CharField(max_length=255)
    NoResponsiva = models.CharField(max_length=255)
    Sucursal = models.CharField(max_length=255)
    NoSerie = models.CharField(max_length=255)
    MarcaEquipo =models.CharField(max_length=255)
    ModeloEquipo =models.CharField(max_length=255)
    RAM = models.IntegerField('RAM',blank=True,null=True)
    

