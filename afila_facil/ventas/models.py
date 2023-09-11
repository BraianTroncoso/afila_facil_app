from django.db import models
from clientes.models import Clientes
from produccion.models import Produccion

# Create your models here.
class Ventas(models.Model):
    cantidad = models.IntegerField(default=0)
    produccion= models.ForeignKey(Produccion, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)