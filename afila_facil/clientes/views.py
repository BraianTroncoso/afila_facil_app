from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes
from .forms import ClientesForm

# Create your views here.
def clientes(request):
    clientes = Clientes.objects.all()
    return render(request,'clientes.html',{'clientes': clientes, 'mensaje': "No hay Clientes"})


def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            detalle = form.cleaned_data['detalle']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            imagen = form.cleaned_data['imagen']

            clientes = Clientes(nombre=nombre, detalle=detalle,
                                  direccion=direccion, telefono=telefono, email=email,
                                  imagen=imagen)
            clientes.save()
            return redirect('clientes')
        else:
            form = ClientesForm()    
    return render(request, 'nuevo_cliente.html')



def editar_cliente(request,id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        form = ClientesForm(request.POST, request.FILES)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.detalle = form.cleaned_data['detalle']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.email = form.cleaned_data['email']
            cliente.imagen = form.cleaned_data['imagen']
            cliente.save()
            return redirect('clientes')
    else:
        form = ClientesForm(initial={
        'nombre': cliente.nombre,
        'detalle': cliente.detalle,
        'direccion': cliente.direccion,
        'telefono':  cliente.telefono,
        'email': cliente.email,
        'imagen': cliente.imagen
        })
    
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})