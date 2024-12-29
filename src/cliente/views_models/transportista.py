from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import TransportistaForm
from ..models import Transportista


class TransportistaListView(ListView):
    model = Transportista

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Transportista.objects.filter(nombre__icontains=busqueda)
        return Transportista.objects.all()


class TransportistaCreateView(CreateView):
    model = Transportista
    form_class = TransportistaForm
    success_url = reverse_lazy('cliente:transportista_list')

    def form_valid(self, form):
        messages.success(self.request, 'El Transportista ha sido creado exitosamente')
        return super().form_valid(form)


class TransportistaUpdateView(UpdateView):
    model = Transportista
    form_class = TransportistaForm
    success_url = reverse_lazy('cliente:transportista_list')

    def form_valid(self, form):
        messages.success(self.request, 'El Transportista ha sido actualizado exitosamente')
        return super().form_valid(form)

class TransportistaDetailView(DetailView):
    model = Transportista

class TransportistaDeleteView(DeleteView):
    model = Transportista
    success_url = reverse_lazy('cliente:transportista_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'El Transportista ha sido eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
