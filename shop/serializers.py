from rest_framework import serializers
from .models import Shop

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'size', 'color', 'quantity', 'price2']
