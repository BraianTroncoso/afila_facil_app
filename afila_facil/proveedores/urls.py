from django.urls import path
from proveedores import views

urlpatterns = [
    path('', views.mostrar_proveedores, name='proveedores'),
    path('nuevo_proveedor/',views.nuevo_proveedor, name='nuevo_proveedor'),
    path('eliminar_proveedor/id<int>', views.eliminar_proveedor, name='eliminar_provedor')
]
