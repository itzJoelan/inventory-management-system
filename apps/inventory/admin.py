from django.contrib import admin
from .models import InventoryMovement, StockAdjustment

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'movement_type', 'quantity', 'created_at']
    list_filter = ['movement_type', 'created_at']

@admin.register(StockAdjustment)
class StockAdjustmentAdmin(admin.ModelAdmin):
    list_display = ['product', 'old_quantity', 'new_quantity', 'reason', 'created_at']
    list_filter = ['created_at']
