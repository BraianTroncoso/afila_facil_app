from django.urls import path
from clientes import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('nuevo_cliente', views.nuevo_cliente, name='nuevo_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente')
]