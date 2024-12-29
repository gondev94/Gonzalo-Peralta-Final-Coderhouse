from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import TransportistaForm
from ..models import Transportista

# **** CATEGORIA - LIST VIEW


def transportista_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Transportista.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = Transportista.objects.all()
    return render(request, 'cliente/transportista_list.html', {'object_list': queryset})


# **** CATEGORIA - CREATE VIEW


def transportista_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = TransportistaForm()
    if request.method == 'POST':
        form = TransportistaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transportista creado exitosamente')
            return redirect('cliente:transportista_list')
    return render(request, 'cliente/transportista_form.html', {'form': form})


# **** CATEGORIA - UPDATE VIEW


def transportista_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transportista.objects.get(id=pk)
    if request.method == 'GET':
        form = TransportistaForm(instance=query)
    if request.method == 'POST':
        form = TransportistaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transportista actualizado exitosamente')
            return redirect('cliente:transportista_list')
    return render(request, 'cliente/transportista_form.html', {'form': form})
                  
# **** CATEGORIA - DETAIL VIEW


def transportista_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transportista.objects.get(id=pk)
    return render(request, 'cliente/transportista_detail.html', {'object': query})


# **** CATEGORIA - DELETE VIEW


def transportista_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Transportista.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        messages.success(request, 'Transportista eliminado exitosamente')
        return redirect('cliente:transportista_list')
    return render(request, 'cliente/transportista_confirm_delete.html', {'object': query})