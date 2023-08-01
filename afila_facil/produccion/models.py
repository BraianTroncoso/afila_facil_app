from django.db import models
from materias_primas.models import Materias

class Produccion(models.Model):
    producto_completo = models.BooleanField(default=False)
    materias = models.ForeignKey(Materias, on_delete=models.CASCADE, related_name='produccion', null=True)
    produccion_cantidad = models.IntegerField(default=0)
    produccion_total = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'produccion'
        verbose_name = "Produccion"

    def __str__(self):
        return f"{self.producto_completo}"



