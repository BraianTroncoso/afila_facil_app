from django import forms
from .models import Produccion
from materias_primas.models import Materias

class ProduccionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    cantidad = forms.IntegerField() #min_value=0 si lo dejo no emitira mensaje

class ProduccionCantidadForm(forms.Form):
    cantidad = forms.IntegerField() #min_value=0 si lo dejo no emitira mensaje
    materias_choices = [(materia.id, materia.nombre) for materia in Materias.objects.all()]
    materias_seleccionadas = forms.MultipleChoiceField(choices=materias_choices, widget=forms.CheckboxSelectMultiple())