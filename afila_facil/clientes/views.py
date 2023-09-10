from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes
from .forms import ClientesForm

# Create your views here.
def clientes(request):
    return render(request,'clientes.html')


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