from django.db import models
from django.contrib.auth.models import User



class Usuario(User):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.telefono} - {self.direccion}'

    