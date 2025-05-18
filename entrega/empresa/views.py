from django.shortcuts import render, get_object_or_404, redirect
from .models import Encargado, Empleado, Cliente
from .forms import EncargadoForm, EmpleadoForm, ClienteForm, BuscarClienteForm

# Create your views here.

def index(request):

    return render( request , "empresa/inicio.html" )


def crear_encargado(request):
    if request.method == 'POST':
        form = EncargadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_encargado')
    else:
        form = EncargadoForm()
    return render(request, 'empresa/form_encargado.html', {'form': form})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'empresa/form_empleado.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_cliente')
    else:
        form = ClienteForm()
    return render(request, 'empresa/form_cliente.html', {'form': form})

def buscar_cliente(request):
    clientes = None
    if request.method == 'POST':
        form = BuscarClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clientes = Cliente.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarClienteForm()
    return render(request, 'empresa/buscar_cliente.html', {'form': form, 'clientes': clientes})
