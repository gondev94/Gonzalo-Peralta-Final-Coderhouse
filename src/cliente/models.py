from django.db import models
from core.models import Usuario


   
class Paquete(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True,blank=True, related_name='paquete')
    descripcion = models.TextField()
    peso = models.FloatField()
    destino = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.descripcion} - {self.peso} - {self.destino}"
        

class Transportista(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    licencia = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.licencia}"

class Flete(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='fletes',null=True,blank=True)
    descripcion = models.TextField(default='default description')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    transportista = models.ForeignKey('Transportista', on_delete=models.CASCADE, related_name='fletes', null=True, blank=True)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE, related_name='flete',null=True,blank=True)

    def __str__(self):
        return f'{self.usuario} - {self.precio}'

class Cotizacion(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
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