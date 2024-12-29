from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Transportista, Paquete, Cotizacion, Flete
from .forms import PaqueteForm



def index(request):
    return render(request, 'cliente/index.html')

def buscar_paquete(request):
    query = request.GET.get('q', '')
    resultados = Paquete.objects.filter(descripcion__icontains=query) if query else []
    return render(request, 'fletes/buscar.html', {'resultados': resultados, 'query': query})


#vistas para transportista
class TransportistaCreateView(CreateView):
    model = Transportista
    fields = ['nombre', 'apellido', 'licencia']
    template_name = 'core/transportista_form.html'
    success_url = reverse_lazy('cliente:transportista_list')


class TransportistaUpdateView(UpdateView):
    model = Transportista
    fields = ['nombre', 'apellido', 'licencia']
    template_name = 'cliente/transportista_form.html'
    success_url = reverse_lazy('cliente:transportista_list')

class TransportistaDeleteView(DeleteView):
    model = Transportista
    template_name = 'cliente/transportista_confirm_delete.html'
    success_url = reverse_lazy('cliente:transportista_list')

class TransportistaListView(ListView):
    model = Transportista
    template_name = 'cliente/transportista_list.html'
    context_object_name = 'transportistas'

#vistas para paquete


class PaqueteCreateView(CreateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = 'cliente/paquete_form.html'
    success_url = reverse_lazy('cliente:paquete_list')  # Cambia según tu configuración


class PaqueteUpdateView(UpdateView):
    model = Paquete
    fields = ['usuario', 'descripcion', 'peso', 'destino']
    template_name = 'cliente/paquete_form.html'
    success_url = reverse_lazy('cliente:paquete_list')

class PaqueteDeleteView(DeleteView):
    model = Paquete
    template_name = 'cliente/paquete_confirm_delete.html'
    success_url = reverse_lazy('cliente:paquete_list')

#vistas para cotizacion de flete

class CotizacionCreateView(CreateView):
    model = Cotizacion
    fields = ['cliente', 'paquete', 'transportista', 'distancia_km', 'precio_por_km']
    template_name = 'cliente/cotizacion_form.html'
    success_url = reverse_lazy('cliente:cotizacion_list')

class CotizacionUpdateView(UpdateView):
    model = Cotizacion
    fields = ['cliente', 'paquete', 'transportista', 'distancia_km', 'precio_por_km', 'total']
    template_name = 'cliente/cotizacion_form.html'
    success_url = reverse_lazy('cliente:cotizacion_list')

class CotizacionDeleteView(DeleteView):
    model = Cotizacion
    template_name = 'cliente/cotizacion_confirm_delete.html'
    success_url = reverse_lazy('cliente:cotizacion_list')
    
class FleteCreateView(CreateView):
    model = Flete
    fields = ['cliente', 'paquete', 'transportista', 'distancia_km', 'precio_por_km']
    template_name = 'cliente/flete_form.html'
    success_url = reverse_lazy('cliente:flete_list')

class FleteUpdateView(UpdateView):
    model = Flete
    fields = ['cliente', 'paquete', 'transportista', 'distancia_km', 'precio_por_km', 'total']
    template_name = 'cliente/flete_form.html'
    success_url = reverse_lazy('cliente:flete_list')

class FleteDeleteView(DeleteView):
    model = Flete
    template_name = 'cliente/flete_confirm_delete.html'
    success_url = reverse_lazy('cliente:flete_list')