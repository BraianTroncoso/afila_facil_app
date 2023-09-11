from django.urls import path
from ventas import views

urlpatterns = [
    path('', views.mostrar_ventas, name='ventas'),
    path('nueva_venta', views.nueva_venta, name='nueva_venta')
]
