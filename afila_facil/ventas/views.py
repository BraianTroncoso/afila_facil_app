from django.shortcuts import render, get_object_or_404, redirect
from .models import Ventas
from .forms import VentasForm
# Create your views here.


def mostrar_ventas(request):
    ventas = Ventas.objects.all()
    return render(request,'ventas.html',{'ventas': ventas, 'mensaje': "No hay Ventas"})

