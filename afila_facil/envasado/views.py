from django.shortcuts import render, get_object_or_404, redirect
from .models import Envasado
from produccion.models import Produccion
from django.contrib import messages
from .forms import EnvasadoForm


# Create your views here.
def mostrar_envasado(request):
    envasado = Envasado.objects.all()
    return render(request, 'mostrar_envasado.html', {'envasado': envasado, 'mensaje': "No hay Tipo de envasado disponible"})

def nuevo_envasado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        envasado = Envasado.objects.create(nombre=nombre)
        return redirect('mostrar_envasado')
    else:
        return render(request, 'nuevo_envasado.html')

def agregar_sub_producto(request):
    return render(request, 'agregar_sub_producto.html')        