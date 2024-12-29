from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import CotizacionForm
from ..models import Cotizacion

# **** CATEGORIA - LIST VIEW


def cotizacion_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Cotizacion.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = Cotizacion.objects.all()
    return render(request, 'cliente/cotizacion_list.html', {'object_list': queryset})


# **** CATEGORIA - CREATE VIEW


def cotizacion_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = CotizacionForm()
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cotización Realizada exitosamente')
            return redirect('cliente:cotizacion_list')
    return render(request, 'cliente/cotizacion_form.html', {'form': form})


# **** CATEGORIA - UPDATE VIEW


def cotizacion_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cotizacion.objects.get(id=pk)
    if request.method == 'GET':
        form = CotizacionForm(instance=query)
    if request.method == 'POST':
        form = CotizacionForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cotización Actualizada exitosamente')
            return redirect('cliente:cotizacion_list')
    return render(request, 'cliente/cotizacion_form.html', {'form': form})


# **** CATEGORIA - DETAIL VIEW


def cotizacion_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cotizacion.objects.get(id=pk)
    return render(request, 'cliente/cotizacion_detail.html', {'object': query})


# **** CATEGORIA - DELETE VIEW


def cotizacion_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Cotizacion.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        messages.success(request, 'Cotizacion Eliminada exitosamente')
        return redirect('cliente:cotizacion_list')
    return render(request, 'cliente/cotizacion_confirm_delete.html', {'object': query})
