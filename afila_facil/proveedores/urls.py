from django.urls import path
from proveedores import views

urlpatterns = [
    path('', views.mostrar_proveedores, name='proveedores'),
    path('nuevo_proveedor/',views.nuevo_proveedor, name='nuevo_proveedor'),
    path('eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('editar/<int:id>/', views.editar_materia, name='editar_proveedor')
]
