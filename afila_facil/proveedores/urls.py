from django.urls import path
from proveedores import views

urlpatterns = [
    path('proveedores/', views.proveedores, name='proveedores'),
    path('nuevo_proveedor/',views.nuevo_proveedor, name='nuevo_proveedor')
]
