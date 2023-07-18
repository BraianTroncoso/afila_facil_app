from django.urls import path
from produccion import views
from materias_primas import urls,views,templates

urlpatterns = [
    path('', views.mostrar_produccion, name='produccion')
    
]
