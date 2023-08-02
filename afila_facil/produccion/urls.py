from django.urls import path
from produccion import views


urlpatterns = [
    path('', views.mostrar_produccion, name='produccion'),
    path('agregar_materias_produccion/',views.agregar_materias_produccion, name='agregar_materias_produccion'),
    path('eliminar_produccion/',views.eliminar_produccion, name='eliminar_produccion'),
    path('finalizar_todos_produccion/', views.finalizar_todos_produccion, name='finalizar_todos_produccion'),
    path('nueva_produccion/',views.nueva_produccion, name='nueva_produccion')
]
