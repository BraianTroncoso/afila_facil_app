from django.shortcuts import render, get_object_or_404
from .models import Productos

def nuevo_producto(request):
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen'].get()

        producto = Productos(nombre=nombre, precio=precio, cantidad=cantidad, descripcion=descripcion, imagen=imagen)
        producto.save()
    return render(request, 'altaProducto.html')


def mostrar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': servicios, 'mensaje': "No hay Productos"})

