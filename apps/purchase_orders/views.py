from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PurchaseOrder, PurchaseOrderItem

@login_required
def purchase_order_list(request):
    orders = PurchaseOrder.objects.all()
    context = {'orders': orders}
    return render(request, 'purchase_orders/list.html', context)

@login_required
def purchase_order_detail(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    return render(request, 'purchase_orders/detail.html', {'order': order})

@login_required
def purchase_order_create(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        expected_delivery = request.POST.get('expected_delivery')
        total_amount = request.POST.get('total_amount')
        notes = request.POST.get('notes')
        
        order = PurchaseOrder.objects.create(
            order_number=f"PO-{PurchaseOrder.objects.count() + 1}",
            supplier_id=supplier_id,
            expected_delivery=expected_delivery,
            total_amount=total_amount,
            notes=notes
        )
        messages.success(request, 'Purchase Order created')
        return redirect('purchase_orders:detail', pk=order.pk)
    
    from apps.suppliers.models import Supplier
    suppliers = Supplier.objects.all()
    return render(request, 'purchase_orders/form.html', {'suppliers': suppliers})

@login_required
def receive_inventory(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        order.status = 'received'
        order.save()
        messages.success(request, 'Inventory received')
        return redirect('purchase_orders:detail', pk=pk)
    return render(request, 'purchase_orders/receive.html', {'order': order})
