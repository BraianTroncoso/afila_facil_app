from django.db import models
from produccion.models import Produccion

class Envasado(models.Model):
    nombre = models.CharField(max_length=100, default='')
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, related_name='envasado', null=True)
    cantidad = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    class Meta:
        db_table = 'envasado'
        verbose_name = "envasado"

    def __str__(self):
        return f"{self.nombre}"
        
    

