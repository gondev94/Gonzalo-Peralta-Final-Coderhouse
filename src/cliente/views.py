from django.shortcuts import render
from . import models



def index(request):
    return render(request, 'cliente/index.html')

def categoria_list(request):
    categorias = models.Categoria.objects.all()
    return render(request, 'cliente/categoria_list.html', {'categorias': categorias})