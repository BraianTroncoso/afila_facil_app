from django.urls import path
from ventas import views

urlpatterns = [
    path('', views.mostrar_ventas, name='ventas'),
]
