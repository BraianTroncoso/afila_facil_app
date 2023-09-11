from django import forms
from produccion.models import Produccion
from clientes.models import Clientes

class VentasForm(forms.Form):
   nombre = forms.CharField(max_length=100)
   clientes = forms.ModelChoiceField(queryset=Clientes.objects.all())
   produccion = forms.ModelChoiceField(queryset=Produccion.objects.all())
   precio = forms.IntegerField()
   cantidad = forms.IntegerField()
   imagen = forms.CharField(max_length=100, required=False)

