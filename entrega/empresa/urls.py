from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('Encargados', views.crear_encargado, name='crear_encargado'),
    path('Empleados', views.crear_empleado, name='crear_empleado'),
    path('Clientes', views.crear_cliente, name='crear_cliente'),
    path('buscar_cliente', views.buscar_cliente, name='buscar_cliente'),
]