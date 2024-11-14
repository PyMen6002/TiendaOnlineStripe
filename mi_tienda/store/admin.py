# store/admin.py

from django.contrib import admin
from .models import Producto, ProductoImagen, Categoria

# Clase inline para agregar imágenes adicionales a los productos
class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1

# Registro de Producto con la configuración personalizada
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenInline]
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)


# Registrar cada modelo individualmente
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoImagen)  # Opcional: solo si deseas ver imágenes como modelo separado


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen')  # Mostrar imagen en la lista
    search_fields = ('nombre', 'descripcion')

admin.site.register(Categoria, CategoriaAdmin)


