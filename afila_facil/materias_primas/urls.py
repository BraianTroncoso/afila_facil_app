from django.urls import path
from materias_primas import views

urlpatterns = [
    path('', views.mostrar_producto, name='productos'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('clientes/', views.clientes, name='clientes')
]
