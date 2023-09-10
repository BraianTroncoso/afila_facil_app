from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=200, blank=True)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100)
    imagen = models.TextField(null=True, blank=True)

    def get_imagen_url(self):
        if self.imagen:
            return f"/static/img/{self.imagen}"
        else:
            return "/static/img/proveedor.png"

    class Meta:
        db_table = 'clientes'
        verbose_name = "Clientes"

    def __str__(self):
        return f"{self.nombre}" 
