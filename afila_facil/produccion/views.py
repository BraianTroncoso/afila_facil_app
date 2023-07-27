from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from materias_primas.models import Productos

# Create your views here.
def mostrar_produccion(request):
    produccion = Produccion.objects.all()#Obtengo una sola instsancia en vez de todas
    return render(request,'produccion.html',{'produccion': produccion, 'mensaje': "No hay Productos en Produccion"})



def crear_instancia_produccion(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')

        if cantidad is not None:
            cantidad = int(cantidad)
            productos = Productos.objects.all()

            #Linea agg por bug - necesito tener mas de una instancia para no tener problemas en la foreignkey
            #produccion = Produccion.objects.create(producto_completo=True, productos=productos[0])
            for producto in productos:
                producto.cantidad -= cantidad
                producto.save()

            produccion = Produccion.objects.first()
            if not produccion:
                produccion = Produccion.objects.create(producto_completo=True)

            produccion.produccion_cantidad += cantidad
            produccion.save()

            total = sum(producto.precio * cantidad for producto in productos)
            produccion.produccion_total += total
            produccion.save()

        else:
            cantidad = 0

        return redirect('produccion')
    else:
        return redirect('produccion')

# VER ESTA PARTE DEL CÓDIGO NUEVAMENTE PORQUE APARENTEMENTE SI SE AGREGA UN PRODUCTO DE CADA UNO
# PERO CUANDO VOY A FINALIZAR TODOS, ESTOS ESTAN RELACIONADOS A UN SOLO ID, ENTONCES CUANDO FINALIZA TODO
# RETORNA LA CANTIDAD SOLAMENTE AL ID 1 Y LOS DEMAS PRODUCTOS NO RECIBEN EL AUMENTO
def eliminar_produccion(request):
    if request.method == 'POST':
        produccion = Produccion.objects.first()
    
        produccion.produccion_cantidad -= 1
        produccion.save()

        productos = Productos.objects.all()
        for producto in productos:
            producto.cantidad += 1
            producto.save()
            produccion.produccion_total -= producto.precio
                
        produccion.save()
        
        return redirect('produccion')
    else:
        return redirect('produccion')


def finalizar_todos_produccion(request):
    if request.method == 'POST':
        produccion = Produccion.objects.first()
        productos = Productos.objects.all()

        if produccion and produccion.productos:
            while produccion.productos and produccion.produccion_cantidad > 0:
                print('bucle ok')
                produccion.produccion_cantidad -= 1
                produccion.save()
                for producto in productos:
                    producto.cantidad += 1
                    producto.save()
                    produccion.produccion_total -= producto.precio
                
        produccion.save()    
        return redirect('produccion')
    else:
        return redirect('produccion')


