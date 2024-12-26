from django.urls import path

from . import views

app_name = 'cliente'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/list', views.categoria_list, name='categoria_list')
]