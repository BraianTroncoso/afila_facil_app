from django.urls import path
from materias_primas import views


urlpatterns = [
    path('nuevo_producto/', view=views.nuevo_servicio, name='nuevo_producto'),
]
