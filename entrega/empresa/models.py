from django.db import models

# Create your models here.


class Encargado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"Bienvenido {self.nombre} {self.apellido}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    area = models.CharField(max_length=50)

    def __str__(self):
        return f"Bienvenido {self.nombre} {self.apellido} - {self.area}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    def __str__(self):
        return f"Bienvenido {self.nombre} {self.apellido} - {self.telefono}"


