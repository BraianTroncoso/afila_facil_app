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
            nuevo_valor = form.cleaned_data['nuevo_valor']
            produccion_id = form.cleaned_data['produccion_seleccionada']
            produccion_seleccionada = Produccion.objects.get(id=produccion_id)
            
            if nueva_cantidad == 0:
                messages.error(request, "No puede ingresar 0 sub producto")
                return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

            if nueva_cantidad < 0:
                messages.error(request, "La cantidad no puede ser negativa")
                return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

            
            valor_produccion = 0
            
            
            if produccion_seleccionada.produccion_cantidad >= nueva_cantidad:
                produccion_seleccionada.produccion_cantidad -= nueva_cantidad
                valor_produccion += produccion_seleccionada.produccion_total  # Acumular el valor total
                produccion_seleccionada.produccion_total -= (produccion_seleccionada.produccion_total * nueva_cantidad)
                produccion_seleccionada.save()

                envasado.cantidad += nueva_cantidad
                envasado.produccion = produccion_seleccionada
                envasado.total += (valor_produccion * nuevo_valor)
                envasado.save()
                return redirect('mostrar_envasado')
                # Cuando haga la vista de editar se le va a poder cambiar el valor del total, acá esta hardcodeada

            else:
                messages.warning(request, f"No hay suficiente stock de {produccion_seleccionada.nombre}")
                return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})
        else:
            form = EnvasadoForm(initial={
                'cantidad': envasado.cantidad
            })
    else:
        form = EnvasadoForm(initial={
            'cantidad': envasado.cantidad
        })

    return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})
