from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Productos

# Create your views here.
def mostrar_produccion(request):
    produccion = Produccion.objects.all()
    return render(request,'produccion.html',{'produccion': produccion, 'mensaje': "No hay Productos en Produccion"})



def crear_instancia_produccion(request):
    if request.method == 'POST':
        # produccion = Produccion.objects.create(producto_completo=True)
        # produccion.save()

        cantidad = request.POST.get('cantidad')

        if cantidad is not None:
            cantidad = int(cantidad)
            productos = Productos.objects.all()

            for producto in productos:
                producto.cantidad -= cantidad
                producto.save()

            # Obtén la instancia existente de Produccion
            produccion = Produccion.objects.first()

            # Incrementa la cantidad en el campo produccion_cantidad
            produccion.produccion_cantidad += cantidad
            produccion.save()

        else:
            cantidad = 0

        return redirect('produccion')
    else:
        return redirect('produccion')




