from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encargado/', views.crear_encargado, name='crear_encargado'),
    path('empleado/', views.crear_empleado, name='crear_empleado'),
    path('cliente/', views.crear_cliente, name='crear_cliente'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
]