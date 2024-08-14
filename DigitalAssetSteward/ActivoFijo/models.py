from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activos(models.Model):
    kace = models.IntegerField('TicketKace',blank=True, null=True)
    categoria = models.CharField(max_length=255)
    usuario_asignado = models.CharField(max_length=255)
    usuario_anterior = models.CharField(max_length=255)
    NoOrdenCompra = models.CharField(max_length=255)
    NoResponsiva = models.CharField(max_length=255)
    Sucursal = models.CharField(max_length=255)
    NoSerie = models.CharField(max_length=255)
    MarcaEquipo =models.CharField(max_length=255)
    ModeloEquipo =models.CharField(max_length=255)
    RAM = models.IntegerField('RAM',blank=True,null=True)
    Almacenamiento = models.IntegerField('Almacenamiento',blank=True, null=True)
    Category = models.CharField(max_length=255)
    WorkSpace = models.CharField(max_length=255)
    NoSerial = models.CharField(max_length=255)
    #Software = models.Choices('Windows')
	#Complementos = models.CharField(max_length=255)
	#FechaCompra = models.DateField()
	#Garantia = models.DateField
	#CostoEquipo = models
	#Tiempo de uso
	#Estado de Garantia (Caducada, Disponible)
	#CER (Lote de compra)

    

