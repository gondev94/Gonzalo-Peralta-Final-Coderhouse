from django.contrib import admin
from .models import Usuario, Paquete, Transportista, Cotizacion, Flete


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['telefono', 'direccion', 'usuario']
       
@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'descripcion', 'peso', 'destino']

@admin.register(Transportista)
class TransportistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'licencia']


@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'paquete', 'transportista', 'distancia_km', 'precio_por_km', 'total']
    
@admin.register(Flete)
class FleteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'descripcion', 'precio', 'transportista', 'paquete']
