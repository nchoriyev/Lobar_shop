from django import forms
from .models import Shop


class OrderForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['size', 'color', 'quantity',]
