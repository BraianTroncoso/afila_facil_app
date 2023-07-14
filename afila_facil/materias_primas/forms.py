from django import forms
from .models import Productos
    
class formularioProducto(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=255, required=True)
    precio = forms.IntegerField(required=True)
    cantidad = forms.IntegerField(required=True)
    imagen= forms.ImageField(required=True)

    class Meta:
            model = Productos

            
class modificarProductoForm(forms.Form):
    nombre = forms.CharField(required=False)
    precio = forms.IntegerField(required=True)
    cantidad = forms.IntegerField(required=True)
    descripcion = forms.CharField(required=True, widget=forms.Textarea)
    imagen= forms.CharField(max_length=100)
     