from django.contrib import admin
from .models import Encargado, Empleado, Cliente

# Register your models here.

admin.site.register(Encargado)
admin.site.register(Empleado)
admin.site.register(Cliente)
