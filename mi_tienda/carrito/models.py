# carrito/models.py

from django.db import models
from store.models import Producto  # Suponiendo que tienes una app de productos llamada "store"

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
