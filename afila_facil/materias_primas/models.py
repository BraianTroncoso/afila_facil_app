from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='static/img')

    class Meta:
        db_table = 'productos'
        verbose_name = "Producto"

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
