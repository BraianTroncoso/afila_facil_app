from django.db import models
from materias_primas.models import Productos

class Produccion(models.Model):
    producto_completo = models.BooleanField(default=False)
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='produccion', null=True)
    produccion_cantidad = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'produccion'
        verbose_name = "Produccion"

    def __str__(self):
        return f"{self.producto_completo}"
