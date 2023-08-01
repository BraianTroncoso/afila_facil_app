from django import forms
from .models import Materias
from proveedores.models import Proveedores
    
class MateriasForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    proveedor = forms.ModelChoiceField(queryset=Proveedores.objects.all())
    precio = forms.IntegerField(required=True)
    cantidad = forms.IntegerField(required=True)
    imagen = forms.CharField(max_length=100, required=False)

    class Meta:
            model = Materias

