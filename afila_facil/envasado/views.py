from django.shortcuts import render, get_object_or_404, redirect
from .models import Envasado
from produccion.models import Produccion
from django.contrib import messages


# Create your views here.
def mostrar_envasado(request):
    envasado = Envasado.objects.all()
    return render(request, 'mostrar_envasado.html', {'envasado': envasado, 'mensaje': "No hay Tipo de envasado disponible"})

