from django.contrib import admin
from .models import PurchaseOrder, PurchaseOrderItem

class PurchaseOrderItemInline(admin.TabularInline):
    model = PurchaseOrderItem

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'supplier', 'order_date', 'status', 'total_amount']
    list_filter = ['status', 'order_date']
    inlines = [PurchaseOrderItemInline]
