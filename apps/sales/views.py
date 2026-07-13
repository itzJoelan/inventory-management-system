from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sale, SaleItem

@login_required
def sales_list(request):
    sales = Sale.objects.all()
    context = {'sales': sales}
    return render(request, 'sales/list.html', context)

@login_required
def sales_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {'sale': sale})

@login_required
def sales_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        total_amount = request.POST.get('total_amount')
        tax = request.POST.get('tax', 0)
        notes = request.POST.get('notes')
        
        sale = Sale.objects.create(
            invoice_number=f"INV-{Sale.objects.count() + 1}",
            customer_id=customer_id if customer_id else None,
            total_amount=total_amount,
            tax=tax,
            notes=notes
        )
        messages.success(request, 'Sale created')
        return redirect('sales:detail', pk=sale.pk)
    
    from apps.customers.models import Customer
    customers = Customer.objects.all()
    return render(request, 'sales/form.html', {'customers': customers})
