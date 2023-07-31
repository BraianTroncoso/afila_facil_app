from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Materias

# Create your views here.


def mostrar_produccion(request):
    # Obtengo una sola instsancia en vez de todas
    produccion = Produccion.objects.all()
    return render(request, 'produccion.html', {'produccion': produccion, 'mensaje': "No hay Materiasen Produccion"})


def crear_instancia_produccion(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        materias = Materias.objects.all()

        if cantidad is not None and cantidad != '' and int(cantidad) > 0:
            cantidad = int(cantidad)
        else:
            cantidad = 0
            return redirect('produccion')

  
        total_materias = sum(materia.cantidad for materia in materias)
        # ver lógica porque acá me está sumando TODAS las materias, y necesito un solo valor para la validacion
        if cantidad < total_materias:
            for materia in materias:
                materia.cantidad -= cantidad
                materia.save()
        else:
            return redirect('produccion')

        produccion = Produccion.objects.first()
        if not produccion:
            produccion = Produccion.objects.create(producto_completo=True)

        produccion.produccion_cantidad += cantidad
        produccion.save()

        total = sum(materia.precio * cantidad for materia in materias)
        produccion.produccion_total += total
        produccion.save()

        return redirect('produccion')
    else:
        return redirect('produccion')


# VER ESTA PARTE DEL CÓDIGO NUEVAMENTE PORQUE APARENTEMENTE SI SE AGREGA UN PRODUCTO DE CADA UNO
# PERO CUANDO VOY A FINALIZAR TODOS, ESTOS ESTAN RELACIONADOS A UN SOLO ID, ENTONCES CUANDO FINALIZA TODO
# RETORNA LA CANTIDAD SOLAMENTE AL ID 1 Y LOS DEMAS PRODUCTOS NO RECIBEN EL AUMENTO


def eliminar_produccion(request):
    if request.method == 'POST':
        produccion = Produccion.objects.first()

        if produccion.produccion_cantidad > 0 and produccion.produccion_total > 0:
            produccion.produccion_cantidad -= 1
            produccion.save()

            materias = Materias.objects.all()
            for materia in materias:
                materia.cantidad += 1
                materia.save()
                produccion.produccion_total -= materia.precio

                produccion.save()

                return redirect('produccion')
        else: 
            return redirect('produccion')
    else:
        return redirect('produccion')


def finalizar_todos_produccion(request):
    if request.method == 'POST':
        produccion = Produccion.objects.first()
        materias = Materias.objects.all()

        if produccion and produccion.materias:
            while produccion.materias and produccion.produccion_cantidad > 0:
                produccion.produccion_cantidad -= 1
                produccion.save()
                for materia in materias:
                    materia.cantidad += 1
                    materia.save()
                    produccion.produccion_total -= materia.precio

        produccion.save()
        return redirect('produccion')
    else:
        return redirect('produccion')

