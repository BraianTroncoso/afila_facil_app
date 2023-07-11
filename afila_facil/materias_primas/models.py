from django.db import models

# Create your models here.
class Widia(models.Model):
    widiaId = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()

class Blister(models.Model):
    blisterId = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()

class Mango(models.Model):
    mangoId = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()

class Carton(models.Model):
    cartonId = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()