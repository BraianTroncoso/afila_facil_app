from django.urls import path
from proveedores import views

urlpatterns = [
    path('proveedores/', views.proveedores, name='clientes')
]
