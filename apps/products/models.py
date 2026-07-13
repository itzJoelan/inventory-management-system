from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('discontinued', 'Discontinued'),
    ]
    
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=100, unique=True, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.SET_NULL, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=10)
    maximum_stock = models.IntegerField(default=100)
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['sku']), models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name
    
    def get_total_value(self):
        return self.stock_quantity * self.cost_price
