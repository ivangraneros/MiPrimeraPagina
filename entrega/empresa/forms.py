from django import forms
from .models import Encargado, Empleado, Cliente

class EncargadoForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class EmpleadoForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    area = forms.CharField(max_length=50)

class ClienteForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()

class BuscarClienteForm(forms.Form):
    nombre = forms.CharField(label='Buscar Cliente por nombre')