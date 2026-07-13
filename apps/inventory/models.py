from django.db import models
from apps.products.models import Product

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('stock_in', 'Stock In'),
        ('stock_out', 'Stock Out'),
        ('adjustment', 'Adjustment'),
        ('transfer', 'Transfer'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()
    reference_number = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"

class StockAdjustment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - Adjustment"
