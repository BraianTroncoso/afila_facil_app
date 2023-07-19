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
        print('Se recibió una solicitud POST')
        print(cantidad)
        if cantidad is not None:
            cantidad = int(cantidad)
            productos = Productos.objects.all()

            for producto in productos:
                producto.cantidad -= cantidad
                producto.save()
        else:
            cantidad = 0
        
        # Resto del código para crear una instancia de Produccion

        return redirect('produccion')
    else:
        return redirect('produccion')


