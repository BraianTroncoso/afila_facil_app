from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Materias
from django.contrib import messages
from .forms import ProduccionForm, ProduccionCantidadForm
from django.http import Http404


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
    ids = []  # Inicializa ids como una lista vacía

    if request.method == 'POST':
        ids_seleccionados = request.POST.get('ids_seleccionados')
        if produccion.produccion_cantidad == 0 and produccion.produccion_total:
            messages.error(request, "No hay productos disponibles")
        if produccion.produccion_cantidad > 0 and produccion.produccion_total > 0:
            produccion.produccion_cantidad -= 1

            # Obtenemos las materias específicas que se van a modificar
            if ids_seleccionados:
                # Haz algo con los IDs aquí
                ids = [int(id) for id in ids_seleccionados.split(',')]
                print(ids)
            
            # Reducimos el total de producción en el precio de la materia
            produccion.produccion_total -= sum(
                materia.precio for materia in ids)

            # Actualizamos las cantidades de las materias sumándoles una unidad
            for materia_id in ids:
                materia = Materias.objects.get(pk=materia_id)
                materia.cantidad += 1
                materia.save()

            produccion.save()
            messages.success(request, "Sub producto eliminado correctamente")
        else:
            Produccion.objects.filter(pk=id).delete()
            produccion = Produccion.objects.all()
            messages.error(request, "Producto eliminado por completo")
    else:
        return redirect('produccion')

    return redirect('produccion')


# def eliminar_produccion(request, id):
#     produccion = get_object_or_404(Produccion, pk=id)

#     if request.method == 'POST':
#         ids_seleccionados = request.POST.get('ids_seleccionados')
#         if produccion.produccion_cantidad == 0 and produccion.produccion_total:
#             messages.error(request, "No hay productos disponibles")
#         if produccion.produccion_cantidad > 0 and produccion.produccion_total > 0:
#             produccion.produccion_cantidad -= 1

            
#             # Obtenemos las materias específicas que se van a modificar
#             # Cuando obtuvimos por ID era para cuando se elimina 1 de producto y este vuelve 1+ a todos
#             # materias = Materias.objects.filter(id__in=[1, 2, 3, 4, 5, 6])
#             if ids_seleccionados:
#             # Haz algo con los IDs aquí
#                 ids = [int(id) for id in ids_seleccionados.split(',')]
#                 print(ids)
#             # Reducimos el total de producción en el precio de la materia

#             produccion.produccion_total -= sum(
#                 materia.precio for materia in ids)

#             # Actualizamos las cantidades de las materias sumándoles una unidad
#             for materia in ids:
#                 materia.cantidad += 1
#                 materia.save()

#             produccion.save()
#             messages.success(request, "Sub producto eliminado correctamente")
#         else:
#             Produccion.objects.filter(pk=id).delete()
#             produccion = Produccion.objects.all()
#             messages.error(request, "Producto eliminado por completo")
#     else:
#         return redirect('produccion')

#     return redirect('produccion')


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
        form = ProduccionCantidadForm(request.POST)
        if form.is_valid():
            nueva_cantidad = form.cleaned_data['cantidad']
          

            if nueva_cantidad == 0:
                messages.error(request, "No puede ingresar 0 materia")
                return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})

            if nueva_cantidad < 0:
                messages.error(request, "La cantidad no puede ser negativa")
                return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})

            ids_seleccionados = form.cleaned_data['materias_seleccionadas']
            print("IDs seleccionados:", ids_seleccionados)
            
            # if nueva_cantidad and not ids_seleccionados:
            #     print("Mensaje de error generado")
            #     return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})


            if not ids_seleccionados:
                messages.error(request, "Tiene que seleccionar alguna materia prima")
                print("Mensaje de error generado")
                return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})

            materias_seleccionadas = Materias.objects.filter(id__in=ids_seleccionados)
            minimo_cantidad_materias = min(materia.cantidad for materia in materias_seleccionadas)

            # if materias_seleccionadas:
            #     produccion.materias.set(materias_seleccionadas)
            #     produccion.save()

            if nueva_cantidad <= minimo_cantidad_materias:
                for materia in materias_seleccionadas:
                    if materia.cantidad >= nueva_cantidad:
                        materia.cantidad -= nueva_cantidad 
                        materia.save()
                    else:
                        messages.warning(request, f"No hay suficiente stock de {materia.nombre}")
                
                nueva_cantidad += produccion.produccion_cantidad
                produccion.produccion_cantidad = nueva_cantidad
                
                total = sum(materia.precio * nueva_cantidad for materia in materias_seleccionadas)
                produccion.produccion_total = total
                produccion.save()
                return redirect('produccion')
            else:
                messages.warning(request, f"No hay suficiente stock, cantidad máxima de {minimo_cantidad_materias} materias primas")
        else:
            return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})
    else:
        form = ProduccionCantidadForm(initial={
            'cantidad': produccion.produccion_cantidad
        })

    return render(request, 'agregar_materias_produccion.html', {'form': form, 'produccion': produccion})
