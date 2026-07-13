from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from apps.products.models import Product
from apps.inventory.models import InventoryMovement
from apps.sales.models import Sale
from apps.purchase_orders.models import PurchaseOrder

@login_required
def dashboard_index(request):
    context = {
        'total_products': Product.objects.count(),
        'low_stock_items': Product.objects.filter(stock_quantity__lt=models.F('minimum_stock')).count(),
        'out_of_stock': Product.objects.filter(stock_quantity=0).count(),
        'total_categories': 0,
        'total_suppliers': 0,
        'total_customers': 0,
    }
    return render(request, 'dashboard/index.html', context)
