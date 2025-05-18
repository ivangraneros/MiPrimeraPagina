from django import forms
from .models import Encargado, Empleado, Cliente

class EncargadoForm(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = ['nombre', 'apellido', 'email']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'area']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono']

class BuscarClienteForm(forms.Form):
    nombre = forms.CharField(label='Buscar Cliente por nombre')