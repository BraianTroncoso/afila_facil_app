from django import forms
from produccion.models import Produccion
from .models import Envasado

class EnvasadoForm(forms.Form):
    cantidad = forms.IntegerField()
    produccion_choices = [(produccion.id, produccion.nombre) for produccion in Produccion.objects.all()]
    produccion_seleccionada = forms.MultipleChoiceField(choices=produccion_choices, widget=forms.CheckboxSelectMultiple())
