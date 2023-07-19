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
            productos = Productos.objects.all()

            for producto in productos:
                producto.cantidad -= cantidad
                producto.save()
        else:
            cantidad = 0

        return redirect('produccion')
    else:
        return redirect('produccion')


