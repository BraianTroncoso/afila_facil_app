from django.shortcuts import render, get_object_or_404
from .models import Productos

def nuevo_producto(request):
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen'].get()

        servicio = Servicios(nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen)
        servicio.save()
    return render(request, 'altaServicio.html')


