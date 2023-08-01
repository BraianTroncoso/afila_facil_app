from django.shortcuts import render

# Create your views here.
def nuevo_proveedor(request):
    if request.method == 'POST':
        

        return render(request, 'nuevo_proveedor.html')

def proveedores(request):
    return render(request,'proveedores.html')