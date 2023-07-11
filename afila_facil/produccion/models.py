from django.db import models
from materias_primas.models import Vidia, Blister, Mango, Carton

class Produccion(models.Model):
    # Atributos de Produccion
    widia = models.ForeignKey(Vidia, on_delete=models.CASCADE)
    blister = models.ForeignKey(Blister, on_delete=models.CASCADE)
    mango = models.ForeignKey(Mango, on_delete=models.CASCADE)
    carton = models.ForeignKey(Carton, on_delete=models.CASCADE)
