from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Materias
from django.contrib import messages
from .forms import AgregarMateriasForm


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


def agregar_materias_produccion(request, produccion_id):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        materias = Materias.objects.all()

        if cantidad is not None and cantidad != '' and int(cantidad) > 0:
            cantidad = int(cantidad)
        else:
            cantidad = 0
            return redirect('produccion')

        minimo_cantidad_materias = min(materia.cantidad for materia in materias)

        if cantidad <= minimo_cantidad_materias:
            for materia in materias:
                materia.cantidad -= cantidad
                materia.save()
        else:
            messages.warning(request, "No hay stock disponible")
            return redirect('agregar_materias_produccion')

        produccion = Produccion.objects.get(id=produccion_id) 

        produccion.produccion_cantidad += cantidad
        produccion.save()

        total = sum(materia.precio * cantidad for materia in materias)
        produccion.produccion_total += total
        produccion.save()
        
        if cantidad > 1:
            mensaje = "{} Producciones agregadas correctamente".format(cantidad)
        if cantidad == 1:
            mensaje = "{} Produccion agregada correctamente".format(cantidad)
        messages.success(request, mensaje)
        return redirect('agregar_materias_produccion')
    else:
        return redirect('agregar_materias_produccion')



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
        return redirect('produccion') # Bug cuando se finaliza no queda el valor 0 - no hace nada
                                      # Es un bug gral, estaria descontando sobre el primer obj en vez de todas las materias  
                                      # También borré la instancia ya creada y se rompió todo  



