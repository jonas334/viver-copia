from django import forms
from apps.tienda.models import Producto, Pedido

class PcForm(forms.ModelForm):
    class Meta:
        modelo = Pedido

        fields = ['productos']
