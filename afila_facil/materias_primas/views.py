from django.shortcuts import render, get_object_or_404
from .models import Productos
from .forms import modificarProductoForm

def nuevo_producto(request):
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen'].get()

        productos = Productos(nombre=nombre, precio=precio, cantidad=cantidad, descripcion=descripcion, imagen=imagen)
        productos.save()
    return render(request, 'altaProducto.html')


def mostrar_producto(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'mensaje': "No hay Productos"})


def eliminarProducto(request, id):
    Productos.objects.filter(pk=id).delete()
    mensaje = "Producto eliminado."
    productos =  Productos.objects.all()
    return render (request, 'productos.html',{'productos':productos, 'mensaje':mensaje})