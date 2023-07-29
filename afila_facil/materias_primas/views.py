from django.shortcuts import render, get_object_or_404, redirect
from .models import Productos
from .forms import ProductoForm


def nueva_materia(request):
    if request.method == 'POST':
        # Pasar los datos del formulario y los archivos adjuntos si los hay
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            cantidad = form.cleaned_data['cantidad']
            descripcion = form.cleaned_data['descripcion']
            imagen = form.cleaned_data['imagen']

            materias = Productos(nombre=nombre, precio=precio,
                                  cantidad=cantidad, descripcion=descripcion, imagen=imagen)
            materias.save()
            return redirect('materias_primas')
    else:
        form = ProductoForm()  # Crear una instancia del formulario en caso de una solicitud GET

    return render(request, 'nueva_materia.html', {'form': form})


def mostrar_materias_primas(request):
    materias = Productos.objects.all()
    return render(request, 'materias_primas.html', {'materias': materias, 'mensaje': "No hay Materia Prima"})



def eliminar_materia(request, id):
    Productos.objects.filter(pk=id).delete()
    mensaje = "Producto eliminado."
    materias = Productos.objects.all()
    return render(request, 'materias_primas.html', {'materias': materias, 'mensaje': mensaje})



def editar_materia(request, id):
    materia = get_object_or_404(Productos, pk=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            materia.nombre = form.cleaned_data['nombre']
            materia.precio = form.cleaned_data['precio']
            materia.cantidad = form.cleaned_data['cantidad']
            materia.descripcion = form.cleaned_data['descripcion']
            materia.imagen = form.cleaned_data['imagen']
            materia.save()
            return redirect('materias_primas')
    else:
        form = ProductoForm(initial={
            'nombre': materia.nombre,
            'precio': materia.precio,
            'cantidad': materia.cantidad,
            'descripcion': materia.descripcion,
            'imagen': materia.imagen
        })

    return render(request, 'editar_materia.html', {'form': form, 'materia': materia})






def clientes(request):
    return render(request,'clientes.html')