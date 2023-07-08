from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request,'tienda/index.html')
def compras(request):
    context={}
    return render(request,'tienda/compras.html')
def registro(request):
    context={}
    return render(request,'tienda/registro.html')