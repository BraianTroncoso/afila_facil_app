from django.urls import path
from produccion import views


urlpatterns = [
    path('produccion', views.mostrar_produccion, name='produccion'),
]
