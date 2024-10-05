from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def Productos(request):
    return render(request,"Productos.html")

def Proveedores(request):
    return render(request,"Proveedores.html")

def Empleados(request):
    return render(request,"Empleados.html")

def Distribuidores(request):
    return render(request,"Distribuidores.html")

def Sucursal(request):
    return render(request,"Sucursal.html")



