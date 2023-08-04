from django.urls import path
from produccion import views


urlpatterns = [
    path('', views.mostrar_produccion, name='produccion'),
    # path('agregar_materias_produccion/<int:produccion_id>/',views.agregar_materias_produccion, name='agregar_materias_produccion'),
    path('eliminar_produccion/',views.eliminar_produccion, name='eliminar_produccion'),
    path('editar/<int:id>/', views.editar_produccion, name='editar_produccion'),
    path('nueva_produccion/',views.nueva_produccion, name='nueva_produccion')
]
