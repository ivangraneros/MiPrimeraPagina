from django.shortcuts import render, get_object_or_404
from .models import Encargado, Empleado, Cliente
from .forms import EncargadoForm, EmpleadoForm, ClienteForm, BuscarClienteForm

# Create your views here.

def index(request):

    return render( request , "empresa/index.html" )


def crear_encargado(request):
    if request.method == 'POST':
        form = EncargadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_encargado')
    else:
        form = EncargadoForm()
    return render(request, 'miapp/crear_encargado.html', {'form': form})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'miapp/crear_empleado.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_cliente')
    else:
        form = ClienteForm()
    return render(request, 'miapp/crear_cliente.html', {'form': form})

def buscar_cliente(request):
    resultados = None
    if request.method == 'POST':
        form = BuscarClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = Cliente.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarClienteForm()
    return render(request, 'miapp/buscar_cliente.html', {'form': form, 'resultados': resultados})
