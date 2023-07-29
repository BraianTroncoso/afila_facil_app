from django.db import models



# Create your models here.
class Materias(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.CharField(max_length=100)


    def get_imagen_url(self):
        if self.imagen:
            return f"/static/img/{self.imagen}"
        else:
            return "/static/img/afilador.jpeg"

    class Meta:
        db_table = 'materias'
        verbose_name = "Materia"

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
