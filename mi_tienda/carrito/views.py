# carrito/views.py

from django.shortcuts import render, redirect
from store.models import Producto
from django.http import HttpResponse
from .models import Carrito
from django.conf import settings
import stripe

#Clave secreta
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    
    # Calcular el total del carrito
    total = sum([item['precio'] * item['cantidad'] for item in carrito])

    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito, 'total': total})

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))
    
    carrito = request.session.get('carrito', [])
    
    # Verificar si el producto ya está en el carrito
    producto_existente = next((item for item in carrito if item['id'] == producto.id), None)
    
    if producto_existente:
        producto_existente['cantidad'] += cantidad
    else:
        carrito.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'descripcion': producto.descripcion,  # Agregar la descripción aquí
            'cantidad': cantidad
        })
    
    request.session['carrito'] = carrito
    return redirect('ver_carrito')


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    
    # Filtrar el carrito para eliminar el producto seleccionado
    carrito = [item for item in carrito if item['id'] != producto_id]
    
    # Actualizar el carrito en la sesión
    request.session['carrito'] = carrito
    
    return redirect('ver_carrito')


def pago_cancelado(request, mensaje=None):
    return render(request, 'carrito/pago_cancelado.html', {
        'mensaje': mensaje or 'El pago no fue procesado. Por favor, inténtalo nuevamente.'
    })

def procesar_pago(request):
    # Obtener el carrito desde la sesión
    carrito_items = request.session.get('carrito', [])

    # Verificar si hay productos en el carrito
    if not carrito_items:
        # Si no hay productos, redirigir con un mensaje adecuado
        return redirect('pago_cancelado', mensaje="No hay artículos en el carrito para procesar el pago.")

    # Calcular el total del carrito
    total = sum(item['precio'] * item['cantidad'] for item in carrito_items)

    # Crear los line_items a partir de los productos en el carrito
    line_items = []
    for item in carrito_items:
        line_items.append({
            'price_data': {
                'currency': 'usd',  # Cambia a la moneda deseada
                'product_data': {
                    'name': item['nombre'],
                    'description': item['descripcion'],  # Asegúrate de que la descripción esté presente
                },
                'unit_amount': int(item['precio'] * 100),  # Convertir el precio a centavos
            },
            'quantity': item['cantidad'],
        })

    try:
        # Crear la sesión de pago de Stripe
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,  # Pasar los productos aquí
            mode='payment',  # Modo de pago
            success_url=request.build_absolute_uri('/pago_exitoso/'),  # Redirigir al éxito
            cancel_url=request.build_absolute_uri('/pago_cancelado/'),  # Redirigir al cancelado
        )

        # Redirigir a la URL de la sesión de Stripe
        return redirect(session.url, code=303)

    except stripe.error.StripeError as e:
        # Capturar el error de Stripe y redirigir con el mensaje de error
        mensaje_error = f"Stripe Error: {e.user_message or e.message}"
        return redirect('pago_cancelado', mensaje=mensaje_error)
