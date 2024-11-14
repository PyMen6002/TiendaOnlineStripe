from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.productos_por_categoria, name='productos_por_categoria'),
    path('', views.lista_productos, name='lista_productos'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'), 
]
