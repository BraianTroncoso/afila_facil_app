from django.shortcuts import render, get_object_or_404, redirect
from .models import Clientes

# Create your views here.
def clientes(request):
    return render(request,'clientes.html')