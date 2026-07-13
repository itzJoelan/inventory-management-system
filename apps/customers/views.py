from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'city', 'country', 'status']

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customers/list.html', context)

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/detail.html', {'customer': customer})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer created successfully')
            return redirect('customers:list')
    else:
        form = CustomerForm()
    return render(request, 'customers/form.html', {'form': form, 'title': 'Create Customer'})

@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully')
            return redirect('customers:detail', pk=pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/form.html', {'form': form, 'customer': customer, 'title': 'Edit Customer'})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully')
        return redirect('customers:list')
    return render(request, 'customers/confirm_delete.html', {'customer': customer})
