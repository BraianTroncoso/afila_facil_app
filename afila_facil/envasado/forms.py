from django import forms
from produccion.models import Produccion
from .models import Envasado

class EnvasadoForm(forms.Form):
    cantidad = forms.IntegerField()
    nuevo_valor = forms.IntegerField()
    produccion_choices = [(produccion.id, produccion.nombre) for produccion in Produccion.objects.all()]
    produccion_seleccionada = forms.ChoiceField(choices=produccion_choices, widget=forms.Select())
