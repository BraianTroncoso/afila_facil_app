from django.urls import path
from materias_primas import views

urlpatterns = [
    path('', views.mostrar_materias_primas, name='materias_primas'),
    path('nueva_materia/', views.nueva_materia, name='nueva_materia'),
    path('editar/<int:id>/', views.editar_materia, name='editar_materia'),
    path('eliminar/<int:id>/', views.eliminar_materia, name='eliminar_materia'),
    path('clientes/', views.clientes, name='clientes')
]
