from django.db import models


class Freight(models.Model):
    client_name = models.CharField(max_length=100)
    package_description = models.TextField()
    distance_km = models.FloatField()
    price_per_km = models.FloatField(default=1400)
    total_price = models.FloatField()

    def save(self, *args, **kwargs):
        # Calcular el precio total antes de guardar
        self.total_price = self.distance_km * self.price_per_km
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.client_name} - {self.package_description}'