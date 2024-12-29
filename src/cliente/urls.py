from django.urls import path
from .views import index
from .views_models import transportista, paquete, cotizacion, flete

app_name = 'cliente'

urlpatterns = [
    path('', index, name='index'),
    path('transportista/list/', transportista.transportista_list, name='transportista_list'),
    path('transportista/create/', transportista.transportista_create, name='transportista_create'),
    path('transportista/update/<int:pk>', transportista.transportista_update, name='transportista_update'),
    path('transportista/detail/<int:pk>', transportista.transportista_detail, name='transportista_detail'),
    path('transportista/delete/<int:pk>', transportista.transportista_delete, name='transportista_delete'),
    path('paquete/list/', paquete.paquete_list, name='paquete_list'),
    path('paquete/create/', paquete.paquete_create, name='paquete_create'),
    path('paquete/update/<int:pk>', paquete.paquete_update, name='paquete_update'),
    path('paquete/detail/<int:pk>', paquete.paquete_detail, name='paquete_detail'),
    path('paquete/delete/<int:pk>', paquete.paquete_delete, name='paquete_delete'),
    path('cotizacion/list/', cotizacion.cotizacion_list, name='cotizacion_list'),
    path('cotizacion/create/', cotizacion.cotizacion_create, name='cotizacion_create'),
    path('cotizacion/update/<int:pk>', cotizacion.cotizacion_update, name='cotizacion_update'),
    path('cotizacion/detail/<int:pk>', cotizacion.cotizacion_detail, name='cotizacion_detail'),
    path('cotizacion/delete/<int:pk>', cotizacion.cotizacion_delete, name='cotizacion_delete'),
    path('flete/list/', flete.flete_list, name='flete_list'),
    path('flete/create/', flete.flete_create, name='flete_create'),
    path('flete/update/<int:pk>', flete.flete_update, name='flete_update'),
    path('flete/detail/<int:pk>', flete.flete_detail, name='flete_detail'),
    path('flete/delete/<int:pk>', flete.flete_delete, name='flete_delete'),
]