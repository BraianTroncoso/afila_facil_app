from django.shortcuts import render, get_object_or_404
from .models import Productos
from .forms import ProductoForm

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
    print("ID:", id)
    producto = get_object_or_404(Productos, pk=id)
    print("Producto:", producto)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        descripcion = request.POST.get('descripcion')
        imagen = request.POST.get('imagen')

        print("Datos del formulario:", nombre, precio, cantidad, descripcion, imagen)

        producto.nombre = nombre
        producto.precio = precio
        producto.cantidad = cantidad
        producto.descripcion = descripcion
        producto.imagen = imagen
        producto.save()

        # Redireccionar a la página de confirmación o a la página de detalles del producto actualizado
        return render(request, 'modificacionProducto.html')

    return render(request, 'modificacionProducto.html')

# def mostrarFormularioProducto(request, id):
#     productos = Productos.objects.only(id =id)
#     return render(request, 'altaProducto.html', {'productos': productos})
#     pass

def clientes(request):
    return render(request,'clientes.html')