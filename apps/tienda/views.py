import json
from django.shortcuts import render, redirect
from django.db.models import Q
from apps.tienda.models import Producto, Categoria, Pedido, Solicitud
from apps.usuario.models import Usuario
from apps.tienda.forms import PcForm
# Create your views here.

def getCategoria(categorias, categoria):
    for c in categorias:
        if c.nombre == categoria:
            return int(c.id)

def productosPorCategoria(request, categoria):
    queryset = request.GET.get('busqueda')
    categorias = Categoria.objects.all()
    id = getCategoria(categorias, categoria)
    productos = Producto.objects.filter(categoria_id=id)
    if queryset:
        productos = Producto.objects.filter(
            Q(categoria_id=id) & (
            Q(nombre__icontains=queryset) | 
            Q(descripcion__icontains=queryset))
        ).distinct()
    return render(request, 'tienda/productos_por_categoria.html', {'productos': productos, 'categorias':categorias, 'categoria':categoria})

def detallesProducto(request,producto_id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id=producto_id)
    productos_similares = Producto.objects.filter(categoria_id=producto.categoria_id)
    return render(request, 'tienda/detalles_producto.html', {
        'producto':producto, 
        'productos_similares': productos_similares, 
        'categorias':categorias
        })

def productores(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    cpus = Producto.objects.filter(categoria_id=1)
    motherboards = Producto.objects.filter(categoria_id=2)
    rams = Producto.objects.filter(categoria_id=3)
    unidadesAlmacenamiento = Producto.objects.filter(categoria_id=4)
    tarjetasVideo = Producto.objects.filter(categoria_id=5)
    monitores = Producto.objects.filter(categoria_id=6)
    teclados = Producto.objects.filter(categoria_id=7)
    mouses = Producto.objects.filter(categoria_id=8)
    gabinetes = Producto.objects.filter(categoria_id=9)
    fuentes = Producto.objects.filter(categoria_id=10)
    if request.method == 'POST':
        form = request.POST
        pedido = Pedido(
            productores = True,
            comprador = request.user
        )
        gabinete = Producto.objects.get(id=form['gabinete'])
        fuente = Producto.objects.get(id=form['fuente'])
        cpu = Producto.objects.get(id=form['cpu'])
        motherboard = Producto.objects.get(id=form['motherboard'])
        ram = Producto.objects.get(id=form['ram'])
        tarjetaVideo = Producto.objects.get(id=form['tarjetaVideo'])
        unidadAlmacenamiento = Producto.objects.get(id=form['unidadAlmacenamiento'])
        monitor = ""
        teclado = ""
        mouse = ""
        if form['monitor'] != "":
            monitor = Producto.objects.get(id=form['monitor'])
            pedido.precio += monitor.precio
        if form['teclado'] != "":
            teclado = Producto.objects.get(id=form['teclado'])
            pedido.precio += teclado.precio
        if form['mouse'] != "":
            mouse = Producto.objects.get(id=form['mouse'])
            pedido.precio += mouse.precio

        pedido.precio += gabinete.precio + fuente.precio + cpu.precio + motherboard.precio + ram.precio + tarjetaVideo.precio + unidadAlmacenamiento.precio
        pedido.save()
        pedido.productos.add(
            gabinete,
            fuente,
            cpu,
            motherboard,
            ram,
            tarjetaVideo,
            unidadAlmacenamiento
        )
        if monitor != "":
            pedido.productos.add(monitor)
        if teclado != "":
            pedido.productos.add(teclado)
        if mouse != "":
            pedido.productos.add(mouse)

    return render(request, 'tienda/productores.html', {
        'categorias':categorias, 
        'productos':productos, 
        'cpus':cpus, 
        'motherboards':motherboards,
        'rams':rams, 
        'unidadesAlmacenamiento':unidadesAlmacenamiento, 
        'tarjetasVideo':tarjetasVideo, 
        'monitores':monitores, 
        'teclados':teclados, 
        'mouses':mouses, 
        'gabinetes':gabinetes, 
        'fuentes':fuentes, 
    })
        


def solicitud(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = request.POST
        solicitud = Solicitud()
        if request.user.is_anonymous:
            solicitud.producto = form['producto-solicitar']
            solicitud.solicitante = form['nombre_noregistrado']
            solicitud.correo = form['correo']
        else:
            solicitud.producto = form['producto-solicitar']
            nombre = request.user
            solicitud.solicitante = nombre
            solicitud.correo = Usuario.objects.get(nombres = request.user).email
        solicitud.save()
        return render(request, 'tienda/solicitud_confirmacion.html', {'categorias':categorias})

    return render(request, 'tienda/solicitud.html', {'categorias':categorias})