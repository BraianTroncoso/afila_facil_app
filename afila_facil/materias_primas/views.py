from django.shortcuts import render, get_object_or_404
from .models import Productos
from .forms import modificarProductoForm

def nuevo_producto(request):
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen']

        productos = Productos(nombre=nombre, precio=precio, cantidad=cantidad, descripcion=descripcion, imagen=imagen)
        productos.save()
    return render(request, 'altaProducto.html')


def mostrar_producto(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'mensaje': "No hay Productos"})


def eliminar_producto(request, id):
    Productos.objects.filter(pk=id).delete()
    mensaje = "Producto eliminado."
    productos = Productos.objects.all()
    return render (request, 'productos.html',{'productos':productos, 'mensaje':mensaje})



def editar_producto(request, id):
    if request.method == 'POST':
            nombre = request.POST['nombre']
            descripcion = request.POST['direccion']
            precio = request.POST['precio']
            cantidad = request.POST['precio']
            imagen = request.POST['imagen']
            
            productos =  Productos(id=id,nombre=nombre, precio=precio, cantidad=cantidad, descripcion=descripcion, imagen=imagen)
            productos.save()
            return redirect('productos')


# def mostrarFormularioProducto(request, id):
#     productos = Productos.objects.only(id =id)
#     return render(request, 'altaProducto.html', {'productos': productos})
#     pass

def clientes(request):
    return render(request,'clientes.html')