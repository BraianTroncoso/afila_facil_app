from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Materias
from django.contrib import messages
from .forms import ProduccionForm


def nueva_produccion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        produccion = Produccion.objects.create(nombre=nombre, producto_completo=True)
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
            produccion.produccion_total -= sum(materia.precio for materia in materias)
            
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
            minimo_cantidad_materias = min(materia.cantidad for materia in materias)

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
                total = sum(materia.precio * nueva_cantidad for materia in materias)
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



# def agregar_materias_produccion(request, produccion_id):
#     if request.method == 'POST':
#         cantidad = request.POST.get('cantidad')
#         materias = Materias.objects.all()

#         if cantidad is not None and cantidad != '' and int(cantidad) > 0:
#             cantidad = int(cantidad)
#         else:
#             cantidad = 0
#             return redirect('agregar_materias_produccion')
#         minimo_cantidad_materias = min(materia.cantidad for materia in materias)

#         if cantidad <= minimo_cantidad_materias:
#             for materia in materias:
#                 materia.cantidad -= cantidad
#                 materia.save()
#         else:
#             messages.warning(request, "No hay stock disponible")
#             return redirect('agregar_materias_produccion')

#         produccion = Produccion.objects.get(id=produccion_id) 

#         produccion.produccion_cantidad += cantidad
#         produccion.save()

#         total = sum(materia.precio * cantidad for materia in materias)
#         produccion.produccion_total += total
#         produccion.save()
        
#         if cantidad > 1:
#             mensaje = "{} Producciones agregadas correctamente".format(cantidad)
#         if cantidad == 1:
#             mensaje = "{} Produccion agregada correctamente".format(cantidad)
#         messages.success(request, mensaje)
#         return redirect('agregar_materias_produccion')
#     else:
#         return redirect('agregar_materias_produccion')

# Realizar nuevamente la funcion de 0, dejar esta de guia. Crear un form como en los demas casos, despues adaparlo porque sino estoy copiando
# Y haciendo cualquier cosa, primero voy hacer que funcione después vemos lo demas.
# En produccion voy a tener Sub producto en donde solo por ahora iria el Afilador
# Despues, eso pasa Envasado y seleccionamos el tipo de envasado
# Despues pasa a producto terminado, y despues se salida de cliente
# Por ultimo vemos el tema del envio si dejamos eso o no, pero lo tenemos ahi



# def finalizar_todos_produccion(request):
#     if request.method == 'POST':
   
#         produccion = Produccion.objects.first()
#         materias = Materias.objects.all()

#         if produccion and produccion.materias:
#             while produccion.materias and produccion.produccion_cantidad > 0:

#                 produccion.produccion_cantidad -= 1
#                 produccion.save()
#                 for materia in materias:
#                     materia.cantidad += 1
#                     materia.save()
#                     produccion.produccion_total -= materia.precio

#         produccion.save()
#         return redirect('produccion')
#     else:
#         return redirect('produccion') # Bug cuando se finaliza no queda el valor 0 - no hace nada
                                      # Es un bug gral, estaria descontando sobre el primer obj en vez de todas las materias  
                                      # También borré la instancia ya creada y se rompió todo  



