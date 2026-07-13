from django.contrib import admin
from .models import Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'customer', 'sale_date', 'status', 'total_amount']
    list_filter = ['status', 'sale_date']
    inlines = [SaleItemInline]
