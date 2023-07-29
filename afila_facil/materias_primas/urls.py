from django.urls import path
from materias_primas import views

urlpatterns = [
    path('', views.mostrar_materias_primas, name='materias_primas'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('editar/<int:id>/', views.editar_materia, name='editar_materia'),
    path('eliminar/<int:id>/', views.eliminar_materia, name='eliminar_materia'),
    path('clientes/', views.clientes, name='clientes')
]
