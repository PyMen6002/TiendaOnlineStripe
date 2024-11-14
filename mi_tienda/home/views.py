# home/views.py
from django.shortcuts import render
from store.models import Producto, Categoria

def home(request):
    # Obtener productos destacados
    productos_destacados = Producto.objects.filter(destacado=True)[:5]  # Filtra los productos destacados
    categorias = Categoria.objects.all()  # Obtener todas las categorías

    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
    }

    return render(request, 'home/index.html', context)
