from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import User


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cliente_usuario_set',  # Unique name for reverse accessor
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cliente_usuario_permissions_set',  # Unique name for reverse accessor
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Paquete(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paquetes')
    descripcion = models.TextField()
    peso = models.FloatField()
    destino = models.CharField(max_length=255)
        

class Transportista(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    licencia = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.licencia}"

class Flete(models.Model):
    nombre = models.CharField(max_length=255, default='default name')
    descripcion = models.TextField(default='default description')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.nombre} - {self.precio}'

class Cotizacion(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    distancia_km = models.FloatField()
    precio_por_km = models.FloatField(default=1400)
    total = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar
        if self.distancia_km and self.precio_por_km:
            self.total = self.distancia_km * self.precio_por_km
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Cliente: {self.cliente}, Total: {self.total}'