from django.shortcuts import render, get_object_or_404, redirect
from .models import Ventas
from .forms import VentasForm
# Create your views here.


def mostrar_ventas(request):
    ventas = Ventas.objects.all()
    return render(request,'ventas.html',{'ventas': ventas})


def nueva_venta(request):
    form = VentasForm(request.POST, request.FILES)
    
    if request.method == 'POST' and form.is_valid():
        clientes = form.cleaned_data['clientes']
        produccion = form.cleaned_data['produccion']
        detalle = form.cleaned_data['detalle']
        cantidad = form.cleaned_data['cantidad']
        costo = form.cleaned_data['costo']
        total = form.cleaned_data['total']

        ventas = Ventas(clientes=clientes, produccion=produccion,
                          detalle=detalle, cantidad=cantidad, costo=costo, total=total)
        ventas.save()
        return redirect('ventas')

    return render(request, 'nueva_venta.html', {'form': form})