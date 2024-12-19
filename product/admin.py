from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_pic' ,'price', 'stock', 'status', 'created_at','sales','active')  # Columns in admin list view
    list_filter = ('status', 'created_at')  # Filters for sidebar
    search_fields = ('name', 'description')  # Search bar for name and description
    ordering = ('-created_at',)  # Default ordering by creation date (descending)