from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'category', 'stock_quantity', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['sku', 'name', 'barcode']
