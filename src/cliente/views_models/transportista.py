from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from ..forms import TransportistaForm
from ..models import Transportista


class TransportistaListView(ListView):
    model = Transportista
    queryset = Transportista.objects.all()
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
        messages.success(self.request, 'Transportista creado exitosamente')
        return super().form_valid(form)


class TransportistaUpdateView(UpdateView):
    model = Transportista
    form_class = TransportistaForm
    success_url = reverse_lazy('cliente:transportista_list')

    def form_valid(self, form):
        messages.success(self.request, 'Transportista actualizado exitosamente')
        return super().form_valid(form)


class TransportistaDetailView(DetailView):
    model = Transportista


class TransportistaDeleteView(DeleteView):
    model = Transportista
    success_url = reverse_lazy('cliente:transportista_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Transportista eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
