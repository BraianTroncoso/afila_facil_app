from django import forms
from .models import Produccion

class ProduccionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    cantidad = forms.IntegerField() #min_value=0 si lo dejo no emitira mensaje

class ProduccionCantidadForm(forms.Form):
    cantidad = forms.IntegerField(min_value=0) #min_value=0 si lo dejo no emitira mensaje
