from django.db import models
from clientes.models import Clientes
from produccion.models import Produccion

# Create your models here.
class Ventas(models.Model):
    cantidad = models.IntegerField(default=0)
    detalle = models.CharField(max_length=200, blank=True)
    produccion= models.ForeignKey(Produccion, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    costo = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    imagen = models.TextField(null=True, blank=True)

    def get_imagen_url(self):
        if self.imagen:
            return f"/static/img/{self.imagen}"
        else:
            return "/static/img/venta.png"