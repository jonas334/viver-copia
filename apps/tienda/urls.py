from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.tienda.views import *

urlpatterns = [
    path('solicitar_producto/', solicitud, name = 'solicitar_producto'),

    path('productores/', productores, name = 'productores'),
    path('<int:producto_id>/', detallesProducto, name = 'detalles_producto'),
    path('<str:categoria>/', productosPorCategoria, name = 'productos_por_categoria'),

]