from django.db import models
from apps.products.models import Product
from apps.suppliers.models import Supplier

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    expected_delivery = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-order_date']
    
    def __str__(self):
        return self.order_number

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_total(self):
        return self.quantity * self.unit_price
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
