from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion

# Create your views here.
def mostrar_produccion(request):
    print('Hola produccion')
    produccion = Produccion.objects.all()
    return render(request,'produccion.html',{'produccion': produccion, 'mensaje': "No hay Productos en Produccion"})