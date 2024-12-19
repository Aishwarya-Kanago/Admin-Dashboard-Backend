from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_pic', 'description', 'price', 'stock', 'status', 'created_at', 'updated_at','sales','active']