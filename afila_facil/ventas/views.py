from django.shortcuts import render, get_object_or_404, redirect
from .models import Ventas
from .forms import VentasForm
# Create your views here.


def mostrar_ventas(request):
    ventas = Ventas.objects.all()
    return render(request,'ventas.html',{'ventas': ventas, 'mensaje': "No hay Ventas"})


def nueva_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST, request.FILES)
        if form.is_valid():
            clientes = form.cleaned_data['clientes']
            produccion = form.cleaned_data['produccion']
            detalle = form.cleaned_data['detalle']
            imagen = form.cleaned_data['imagen']
            cantidad = form.cleaned_data['cantidad']
            costo = form.cleaned_data['costo']
            total = form.cleaned_data['total']

            ventas = Ventas(clientes=clientes, produccion=produccion,
                                  detalle=detalle, cantidad=cantidad, costo=costo, total=total,
                                  imagen=imagen)
            ventas.save()
            return redirect('ventas')
        else:
            form = VentasForm()    
    return render(request, 'nueva_venta.html', {'form': form})