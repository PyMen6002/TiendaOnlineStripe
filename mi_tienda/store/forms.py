# store/forms.py
from django import forms
from .models import Producto  # Asegúrate de tener el modelo `Producto`

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Incluye todos los campos del modelo Producto
