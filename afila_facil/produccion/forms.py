from django import forms
from .models import Produccion

class AgregarMateriasForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)

    def __init__(self, *args, produccion=None, **kwargs):
        super(AgregarMateriasForm, self).__init__(*args, **kwargs)
        if produccion:
            self.fields['produccion'] = forms.ModelChoiceField(queryset=Produccion.objects.filter(id=produccion.id), empty_label=None)
