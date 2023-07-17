from django import forms
from .models import Productos
    
class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=255, required=True, widget=forms.Textarea)
    precio = forms.IntegerField(required=True)
    cantidad = forms.IntegerField(required=True)
    imagen= forms.ImageField(required=False)

    class Meta:
            model = Productos

