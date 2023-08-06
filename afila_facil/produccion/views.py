from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Materias
from django.contrib import messages
from .forms import ProduccionForm


def nueva_produccion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        produccion = Produccion.objects.create(
            nombre=nombre, producto_completo=True)
        return redirect('produccion')
    else:
        return render(request, 'nueva_produccion.html')


def mostrar_produccion(request):
    produccion = Produccion.objects.all()
    return render(request, 'produccion.html', {'produccion': produccion, 'mensaje': "No hay Materias en Produccion"})


def eliminar_produccion(request, id):
    produccion = get_object_or_404(Produccion, pk=id)

    if request.method == 'POST':
        if produccion.produccion_cantidad > 0 and produccion.produccion_total > 0:
            # Restamos una unidad de producción
            produccion.produccion_cantidad -= 1

            # Obtenemos las materias específicas que se van a modificar
            materias = Materias.objects.filter(id__in=[1, 2, 3, 4, 5, 6])

            # Reducimos el total de producción en el precio de la materia
            produccion.produccion_total -= sum(
                materia.precio for materia in materias)

            # Actualizamos las cantidades de las materias sumándoles una unidad
            for materia in materias:
                materia.cantidad += 1
                materia.save()

            produccion.save()
            messages.success(request, "Sub producto eliminado correctamente")
        else:
            messages.error(request, "No es posible eliminar sino hay stock")
    else:
        return redirect('produccion')

    return redirect('produccion')


def editar_produccion(request, id):
    produccion = get_object_or_404(Produccion, pk=id)

    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            nueva_nombre = form.cleaned_data['nombre']
            nueva_cantidad = form.cleaned_data['cantidad']

            if nueva_cantidad < 0:
                messages.error(request, "La cantidad no puede ser negativa")
                return render(request, 'editar_produccion.html', {'form': form, 'produccion': produccion})

            # Obtener las materias específicas que se van a modificar
            materias = Materias.objects.filter(id__in=[1, 2, 3, 4, 5, 6])
            # Calcular el mínimo de cantidad de materias
            minimo_cantidad_materias = min(
                materia.cantidad for materia in materias)

            # Verificar si hay suficiente stock
            if nueva_cantidad <= minimo_cantidad_materias:
                # Calcular la diferencia entre la nueva cantidad y la cantidad anterior
                diferencia_cantidad = nueva_cantidad - produccion.produccion_cantidad

                # Actualizar las cantidades de las materias
                for materia in materias:
                    materia.cantidad -= diferencia_cantidad
                    materia.save()

                # Actualizar la cantidad de producción con el nuevo valor
                produccion.produccion_cantidad = nueva_cantidad
                produccion.nombre = nueva_nombre

                # Calcular y actualizar el total
                total = sum(materia.precio *
                            nueva_cantidad for materia in materias)
                produccion.produccion_total = total

                produccion.save()

                return redirect('produccion')
            else:
                messages.warning(request, "No hay stock disponible")
    else:
        form = ProduccionForm(initial={
            'nombre': produccion.nombre,
            'cantidad': produccion.produccion_cantidad,
        })

    return render(request, 'editar_produccion.html', {'form': form, 'produccion': produccion})


def agregar_materias_produccion(request, id):
    produccion = get_object_or_404(Produccion, pk=id)
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            nueva_cantidad = form.cleaned_data['cantidad']

            if nueva_cantidad < 0:
                messages.error(request, "La cantidad no puede ser negativa")
                return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})

            # Obtener las materias específicas que se van a modificar
            materias = Materias.objects.filter(id__in=[1, 2, 3, 4, 5, 6])
            # Calcular el mínimo de cantidad de materias
            minimo_cantidad_materias = min(
                materia.cantidad for materia in materias)
      
            if nueva_cantidad <= minimo_cantidad_materias:
                for materia in materias:
                    materia.cantidad -= nueva_cantidad 
                    materia.save()
                produccion.produccion_cantidad = nueva_cantidad
                # Calcular y actualizar el total
                total = sum(materia.precio *
                            nueva_cantidad for materia in materias)
                produccion.produccion_total = total
                produccion.save()
            else:
                messages.warning(request, "No hay stock disponible")
                return redirect('agregar_materias_produccion') 
    else:
        return redirect('produccion')



