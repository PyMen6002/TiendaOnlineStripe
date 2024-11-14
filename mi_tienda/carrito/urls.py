# carrito/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),  # Página de ver el carrito
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),  # Ruta para agregar producto
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),  # Ruta para eliminar producto
    path('carrito/procesar_pago/', views.procesar_pago, name='procesar_pago'),
    path('pago_cancelado/<str:mensaje>/', views.pago_cancelado, name='pago_cancelado'),
]
