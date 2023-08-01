from django import forms
from proveedores.models import Proveedores

class MateriasForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    proveedores = forms.ModelChoiceField(queryset=Proveedores.objects.all())
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()
    imagen = forms.CharField(max_length=100, required=False)



