from django import forms
from .models import Cotizacion, Flete, Paquete, Transportista

def validar_nombre(nombre: str):
    if len(nombre) < 3:
        raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
    if not nombre.isalpha():
        raise forms.ValidationError('El nombre solo puede contener letras')
    return nombre

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['cliente', 'paquete', 'transportista', 'distancia_km', 'precio_por_km']
        

class FleteForm(forms.ModelForm):
    class Meta:
        model = Flete
        fields = ['usuario', 'descripcion', 'precio', 'transportista', 'paquete']
    
class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['descripcion', 'peso', 'destino']
        
    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')
        return validar_nombre(nombre)


class TransportistaForm(forms.ModelForm):
    nombre = forms.CharField(validators=[validar_nombre])
    class Meta:
        model = Transportista
        fields = ['nombre', 'apellido', 'licencia']

