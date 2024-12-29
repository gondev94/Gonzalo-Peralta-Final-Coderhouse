from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import FleteForm
from ..models import Flete


def flete_list(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Flete.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = Flete.objects.all()
    return render(request, 'cliente/flete_list.html', {'object_list': queryset})


def flete_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = FleteForm()
    if request.method == 'POST':
        form = FleteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flete creado exitosamente')
            return redirect('cliente:flete_list')
    return render(request, 'cliente/flete_form.html', {'form': form})


def flete_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = Flete.objects.get(id=pk)
    if request.method == 'GET':
        form = FleteForm(instance=query)
    if request.method == 'POST':
        form = FleteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Flete actualizado exitosamente')
            return redirect('cliente:flete_list')
    return render(request, 'cliente/flete_form.html', {'form': form})



def flete_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Flete.objects.get(id=pk)
    return render(request, 'cliente/flete_detail.html', {'object': query})



def flete_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Flete.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        messages.success(request, 'Flete Eliminado exitosamente')
        return redirect('cliente:flete_list')
    return render(request, 'cliente/flete_confirm_delete.html', {'object': query})
