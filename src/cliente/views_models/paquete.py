from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from ..forms import PaqueteForm
from ..models import Paquete
from django.shortcuts import render, redirect


def paquete_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Paquete.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = Paquete.objects.all()
    return render(request, 'cliente/paquete_list.html', {'object_list': queryset})


def paquete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = PaqueteForm()
    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paquete creado exitosamente')
            return redirect('cliente:paquete_list')
    return render(request, 'cliente/paquete_form.html', {'form': form})


def paquete_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Paquete.objects.get(id=pk)
    if request.method == 'GET':
        form = PaqueteForm(instance=query)
    if request.method == 'POST':
        form = PaqueteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paquete actualizado exitosamente')
            return redirect('cliente:paquete_list')
    return render(request, 'cliente/paquete_form.html', {'form': form})


def paquete_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Paquete.objects.get(id=pk)
    return render(request, 'cliente/paquete_detail.html', {'object': query})


def paquete_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Paquete.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        messages.success(request, 'Paquete eliminado exitosamente')
        return redirect('cliente:paquete_list')
    return render(request, 'cliente/paquete_confirm_delete.html', {'object': query})
