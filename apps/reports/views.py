from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.products.models import Product
from apps.sales.models import Sale
from apps.purchase_orders.models import PurchaseOrder

@login_required
def reports_list(request):
    return render(request, 'reports/list.html')

@login_required
def inventory_report(request):
    products = Product.objects.all()
    total_value = sum(p.get_total_value() for p in products)
    context = {'products': products, 'total_value': total_value}
    return render(request, 'reports/inventory.html', context)

@login_required
def sales_report(request):
    sales = Sale.objects.all()
    total_sales = sum(s.total_amount for s in sales)
    context = {'sales': sales, 'total_sales': total_sales}
    return render(request, 'reports/sales.html', context)

@login_required
def purchase_report(request):
    orders = PurchaseOrder.objects.all()
    total_purchases = sum(o.total_amount for o in orders)
    context = {'orders': orders, 'total_purchases': total_purchases}
    return render(request, 'reports/purchases.html', context)
