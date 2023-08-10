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

def agregar_sub_producto(request, id):
    envasado = get_object_or_404(Envasado, pk=id)

    if request.method == 'POST':
        form = EnvasadoForm(request.POST)
        if form.is_valid():
            nueva_cantidad = form.cleaned_data['cantidad']

            if nueva_cantidad == 0:
                messages.error(request, "No puede ingresar 0 sub producto")
                return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

            if nueva_cantidad < 0:
                messages.error(request, "La cantidad no puede ser negativa")
                return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

            ids_seleccionados = form.cleaned_data['produccion_seleccionada']

            produccion_seleccionada = Produccion.objects.filter(id__in=ids_seleccionados)
            nuevo_valor = 100
            
            for produccion in produccion_seleccionada:
                if produccion.produccion_cantidad >= nueva_cantidad:
                    produccion.produccion_cantidad -= nueva_cantidad
                    produccion.save()
                else:
                    messages.warning(request, f"No hay suficiente stock de {produccion.nombre}")
                    return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

            envasado.cantidad += nueva_cantidad
            total = sum(produccion.produccion_total * nuevo_valor for produccion in produccion_seleccionada)
            envasado.total = total    
            envasado.save()

            return redirect('mostrar_envasado')
        else:
            form = EnvasadoForm(initial={
                'cantidad': envasado.cantidad
            })
    else:
        form = EnvasadoForm(initial={
            'cantidad': envasado.cantidad
        })

    return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})
