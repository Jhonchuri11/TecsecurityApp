from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    numero = models.CharField(max_length=9)
    password = models.CharField(max_length=255, unique=True)

    REQUIRED_FIELDS = ['email']

class Calle(models.Model):
    nombres = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    nivelSeguridad = models.IntegerField()


class Comentario(models.Model):
    idCalle = models.ForeignKey(Calle, on_delete=models.CASCADE)
    comentario = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class Incidentes(models.Model):
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    descripcion = models.TextField()
    aprobado = models.BooleanField(default=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class CallePeligrosas(models.Model):
    nombre = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)
    descripcion = models.TextField()
    nivelPeligro = models.IntegerField()

    
    
