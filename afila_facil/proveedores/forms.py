from django import forms
from .models import Proveedores
    
class ProveedoresForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    direccion = forms.CharField(max_length=100, required=True)
    telefono = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    imagen = forms.CharField(max_length=100, required=False)

    class Meta:
            model = Proveedores
