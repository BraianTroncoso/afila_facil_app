from django.urls import path
from materias_primas import views

urlpatterns = [
    path('clientes/', views.clientes, name='clientes')
]
