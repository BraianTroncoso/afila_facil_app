from django.urls import path
from clientes import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
]