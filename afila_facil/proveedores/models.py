from django.db import models
from produccion.models import Produccion

# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    tel = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    imagen = models.TextField(null=True, blank=True)
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name='produccion', null=True)

    def get_imagen_url(self):
        if self.imagen:
            return f"/static/img/{self.imagen}"
        else:
            return "/static/img/afilador.jpeg"

    class Meta:
        db_table = 'proveedores'
        verbose_name = "Proveedores"