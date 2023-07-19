from django.urls import path
from produccion import views


urlpatterns = [
    path('', views.mostrar_produccion, name='produccion'),
]
