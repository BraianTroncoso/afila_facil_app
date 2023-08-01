from django.db import models
from produccion.models import Produccion

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    tel = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name='produccion', null=True)


    class Meta:
        db_table = 'proveedores'
        verbose_name = "Proveedores"