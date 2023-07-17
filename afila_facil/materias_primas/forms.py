from django import forms
from .models import Productos
    
class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    descripcion = forms.CharField(max_length=255, required=False, widget=forms.Textarea)
    precio = forms.IntegerField(required=False)
    cantidad = forms.IntegerField(required=False)
    imagen= forms.ImageField(required=False)

    class Meta:
            model = Productos

