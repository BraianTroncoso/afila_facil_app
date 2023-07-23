from django.urls import path
from produccion import views


urlpatterns = [
    path('', views.mostrar_produccion, name='produccion'),
    path('crear_instancia_produccion/',views.crear_instancia_produccion, name='crear_instancia_produccion'),
    path('eliminar_produccion/',views.eliminar_produccion, name='eliminar_produccion'),
    path('finalizar_todos_produccion', views.finalizar_todos_produccion, name='finalizar_todos_produccion')
]
