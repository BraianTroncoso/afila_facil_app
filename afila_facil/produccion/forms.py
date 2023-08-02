from django import forms
from .models import Produccion

class SeleccionProduccionForm(forms.Form):
    cantidad = forms.IntegerField()
    produccion_id = forms.ModelChoiceField(queryset=Produccion.objects.all(), empty_label=None)
