from django.urls import path
from envasado import views

urlpatterns = [
    path('', views.mostrar_envasado, name='mostrar_envasado'),
    path('nuevo_envasado/', views.nuevo_envasado, name='nuevo_envasado'),
    path('agregar_sub_producto/<int:id>/', views.agregar_sub_producto, name='agregar_sub_producto')
]
