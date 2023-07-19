from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Productos

# Create your views here.
def mostrar_produccion(request):
    produccion = Produccion.objects.all()
    return render(request,'produccion.html',{'produccion': produccion, 'mensaje': "No hay Productos en Produccion"})


def crear_instancia_produccion(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        if cantidad is not None:
            cantidad = int(cantidad)
        else:
            cantidad = 0

        productos = Productos.objects.all()
        for producto in productos:
            producto.cantidad -= cantidad
            producto.save()

        # Obtén un objeto Productos específico para asignarlo al campo productos en Produccion
        producto_referencia = get_object_or_404(Productos, id=1)

        produccion = Produccion.objects.create(producto_completo=True, productos=producto_referencia)
        produccion.save()

        return redirect('produccion')
    else:
        return redirect('produccion')
