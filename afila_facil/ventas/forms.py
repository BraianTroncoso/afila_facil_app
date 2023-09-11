from django import forms
from produccion.models import Produccion
from clientes.models import Clientes

class VentasForm(forms.Form):
   clientes = forms.ModelChoiceField(queryset=Clientes.objects.all())
   produccion = forms.ModelChoiceField(queryset=Produccion.objects.all())
   detalle = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea()
    )
   cantidad = forms.IntegerField()
   costo = forms.IntegerField()
   total = forms.IntegerField()

   class Meta:
            model = Clientes