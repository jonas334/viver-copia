from django.contrib import admin
from apps.tienda.models import Categoria, Producto, Pedido, Solicitud

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id', 'nombre']

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'categoria']
    list_display = ['id', 'nombre', 'precio', 'cantidad', 'fecha_creacion', 'fecha_actualizacion', 'categoria_id']

class PedidoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'comprador']
    list_display = ['id', 'comprador', 'precio', 'fecha_pedido']

class SolicitudAdmin(admin.ModelAdmin):
    search_fields = ['id', 'solicitante']
    list_display = ['id', 'solicitante', 'producto', 'fecha_solicitud', 'correo']

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Solicitud,SolicitudAdmin)