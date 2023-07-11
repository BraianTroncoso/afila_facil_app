from django.urls import path
from materias_primas import views


urlpatterns = [
    path('', view=views.mostrar_producto, name='productos'),
    path('nuevo_producto/', view=views.nuevo_producto, name='nuevo_producto'),

]
