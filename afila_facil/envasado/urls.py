from django.urls import path
from envasado import views

urlpatterns = [
    path('', views.mostrar_envasado, name='mostrar_envasado')
]
