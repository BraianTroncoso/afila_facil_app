# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Envasado
# from produccion.models import Produccion
# from django.contrib import messages
# from .forms import EnvasadoForm


# # Create your views here.
# def mostrar_envasado(request):
#     envasado = Envasado.objects.all()
#     return render(request, 'mostrar_envasado.html', {'envasado': envasado, 'mensaje': "No hay Tipo de envasado disponible"})

# def nuevo_envasado(request):
#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         envasado = Envasado.objects.create(nombre=nombre)
#         return redirect('mostrar_envasado')
#     else:
#         return render(request, 'nuevo_envasado.html')

# def agregar_sub_producto(request, id):
#     envasado = get_object_or_404(Envasado, pk=id)

#     if request.method == 'POST':
#         form = EnvasadoForm(request.POST)
#         if form.is_valid():
#             nueva_cantidad = form.cleaned_data['cantidad']
#             nuevo_valor = form.cleaned_data['nuevo_valor']
#             #if not envasado.produccion:
#             produccion_id = form.cleaned_data['produccion_seleccionada']
#             produccion_seleccionada = Produccion.objects.get(id=produccion_id)
            
#             if nueva_cantidad == 0:
#                 messages.error(request, "No puede ingresar 0 sub producto")
#                 return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

#             if nueva_cantidad < 0:
#                 messages.error(request, "La cantidad no puede ser negativa")
#                 return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

#             valor_produccion = 0
                
#             if produccion_seleccionada.produccion_cantidad >= nueva_cantidad:
#                 descuento_valor = (nueva_cantidad / produccion_seleccionada.produccion_cantidad) * produccion_seleccionada.produccion_total
#                 produccion_seleccionada.produccion_total -= descuento_valor
#                 produccion_seleccionada.produccion_cantidad -= nueva_cantidad
#                 produccion_seleccionada.save()

#                 envasado.cantidad += nueva_cantidad
#                 envasado.produccion = produccion_seleccionada
#                 envasado.total += (nuevo_valor * descuento_valor)
#                 envasado.save()
#                 return redirect('mostrar_envasado')
#             else:
#                 messages.warning(request, f"No hay suficiente stock de {produccion_seleccionada.nombre}")
#                 return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})
#         else:
#             form = EnvasadoForm(initial={
#                 'cantidad': envasado.cantidad
#             })
#     else:
#         form = EnvasadoForm(initial={
#             'cantidad': envasado.cantidad
#         })

#     return render(request, 'agregar_sub_producto.html', {'form': form, 'envasado': envasado})

# def editar_envasado(request, id):
#     envasado = get_object_or_404(Envasado, pk=id)

#     if request.method == 'POST':
#         form = EnvasadoForm(request.POST, request.FILES)
#         if form.is_valid():
#             envasado.nombre = form.cleaned_data['nombre']
#             envasado.nueva_cantidad = form.cleaned_data['cantidad']
#             envasado.nuevo_valor = form.cleaned_data['nuevo_valor']
#             produccion_id = form.cleaned_data['produccion_seleccionada']
#             produccion_seleccionada = Produccion.objects.get(id=produccion_id)
#             return redirect('mostrar_envasado')
#     else:
#         form = MateriasForm(initial={
#             'nombre': envasado.nombre,
#             'cantidad': envasado.cantidad,
#             'nuevo_valor': envasado.nuevo_valor,
#             'produccion_seleccionada': envasado.produccion_id
#         })

#     return render(request, 'editar_envasado.html', {'form': form, 'materia': materia})

# Volver a ver la lógica, seguro hay un error con el tema del producto o editar, igual, tampoco puedo seguir sino se si tiene un precio
# total o que.
# Tambien ver el bug de cuando se selecciona un elemento a, este mismo supera los 100vh y rompe todo.
# Me volvi a fijar y sigue todo igual, tengo que volver a ver la lógica para ver como puedo finalizarlo
# Pero tengo que esperar al Lisandro a ver que me dice