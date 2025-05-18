from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('', views.index),
    path('Encargados', views.crear_encargado, name='nuevo_encargado'),
    path('Empleados', views.crear_empleado, name='nuevo_empleado'),
    path('Clientes', views.crear_cliente, name='nuevo_cliente'),
    path('buscar_cliente', views.buscar_cliente, name='buscar_cliente'),
]