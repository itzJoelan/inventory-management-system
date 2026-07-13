from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.products.models import Product
from .models import InventoryMovement, StockAdjustment

@login_required
def inventory_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/list.html', context)

@login_required
def stock_in(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 0))
        reference = request.POST.get('reference')
        notes = request.POST.get('notes')
        
        product = Product.objects.get(id=product_id)
        product.stock_quantity += quantity
        product.save()
        
        InventoryMovement.objects.create(
            product=product,
            movement_type='stock_in',
            quantity=quantity,
            reference_number=reference,
            notes=notes
        )
        messages.success(request, 'Stock added successfully')
        return redirect('inventory:list')
    
    products = Product.objects.all()
    return render(request, 'inventory/stock_in.html', {'products': products})

@login_required
def stock_out(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 0))
        reference = request.POST.get('reference')
        notes = request.POST.get('notes')
        
        product = Product.objects.get(id=product_id)
        if product.stock_quantity >= quantity:
            product.stock_quantity -= quantity
            product.save()
            
            InventoryMovement.objects.create(
                product=product,
                movement_type='stock_out',
                quantity=quantity,
                reference_number=reference,
                notes=notes
            )
            messages.success(request, 'Stock removed successfully')
        else:
            messages.error(request, 'Insufficient stock')
        
        return redirect('inventory:list')
    
    products = Product.objects.all()
    return render(request, 'inventory/stock_out.html', {'products': products})

@login_required
def stock_adjustment(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_quantity = int(request.POST.get('new_quantity', 0))
        reason = request.POST.get('reason')
        
        product = Product.objects.get(id=product_id)
        old_quantity = product.stock_quantity
        product.stock_quantity = new_quantity
        product.save()
        
        StockAdjustment.objects.create(
            product=product,
            old_quantity=old_quantity,
            new_quantity=new_quantity,
            reason=reason
        )
        messages.success(request, 'Stock adjusted successfully')
        return redirect('inventory:list')
    
    products = Product.objects.all()
    return render(request, 'inventory/adjustment.html', {'products': products})

@login_required
def inventory_history(request):
    movements = InventoryMovement.objects.all()
    context = {'movements': movements}
    return render(request, 'inventory/history.html', context)
