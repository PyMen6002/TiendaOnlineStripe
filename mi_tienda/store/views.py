from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Producto, Categoria

def lista_productos(request):
    # Obtener el ID de la categoría desde los parámetros GET de la URL
    categoria_id = request.GET.get('category')

    # Si se seleccionó una categoría, filtrar los productos por esa categoría
    if categoria_id:
        categoria = Categoria.objects.get(id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria)
        categoria_nombre = categoria.nombre
    else:
        # Si no se seleccionó ninguna categoría, mostrar todos los productos
        productos = Producto.objects.all()
        categoria_nombre = "Todas las Categorías"
    
    return render(request, 'store/lista_productos.html', {
        'productos': productos,
        'categoria_nombre': categoria_nombre,
    })


from .forms import ProductoForm

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    imagenes = producto.imagenes.all()  # Recupera todas las imágenes relacionadas
    return render(request, 'store/detalle_producto.html', {'producto': producto, 'imagenes': imagenes})


def productos_por_categoria(request):
    # Obtener el ID de la categoría desde la URL (parámetro de la query string)
    categoria_id = request.GET.get('category')
    
    # Si se pasa el ID de la categoría, se filtran los productos de esa categoría
    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria)
        categoria_nombre = categoria.nombre  # Se pasa el nombre de la categoría
    else:
        # Si no se pasa categoría, se muestran todos los productos
        productos = Producto.objects.all()
        categoria_nombre = 'Todas las Categorías'  # Nombre por defecto

    context = {
        'productos': productos,
        'categoria_nombre': categoria_nombre,  # Pasamos el nombre de la categoría al template
    }
    
    return render(request, 'store/productos_por_categoria.html', context)