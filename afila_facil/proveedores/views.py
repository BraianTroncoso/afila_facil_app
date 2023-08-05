from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedores
from .forms import ProveedoresForm
# Create your views here.
def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedoresForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            imagen = form.cleaned_data['imagen']

            proveedores = Proveedores(nombre=nombre, apellido=apellido,
                                  direccion=direccion, telefono=telefono, email=email,
                                  imagen=imagen)
            proveedores.save()
            return redirect('proveedores')
        else:
            form = ProveedoresForm()    
    return render(request, 'nuevo_proveedor.html')


def mostrar_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request,'proveedores.html',{'proveedores': proveedores, 'mensaje': "No hay Proveedores"})


def eliminar_proveedor(request,id):
    Proveedores.objects.filter(pk=id).delete()
    proveedores = Proveedores.objects.all()
    return render(request,'proveedores.html',{'proveedores': proveedores, 'mensaje': "No hay Proveedores"})


def editar_proveedor(request,id):
    proveedor = get_object_or_404(Proveedores, pk=id)
    if request.method == 'POST':
        form = ProveedoresForm(request.POST, request.FILES)
        if form.is_valid():
            proveedor.nombre = form.cleaned_data['nombre']
            proveedor.apellido = form.cleaned_data['apellido']
            proveedor.direccion = form.cleaned_data['direccion']
            proveedor.telefono = form.cleaned_data['telefono']
            proveedor.email = form.cleaned_data['email']
            proveedor.imagen = form.cleaned_data['imagen']
            proveedor.save()
            return redirect('proveedores')
    else:
        form = ProveedoresForm(initial={
        'nombre': proveedor.nombre,
        'apellido': proveedor.apellido,
        'direccion': proveedor.direccion,
        'telefono':  proveedor.telefono,
        'email': proveedor.email,
        'imagen': proveedor.imagen
        })
    
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})