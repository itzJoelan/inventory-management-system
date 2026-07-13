from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_person', 'phone', 'email', 'address', 'company', 'status']

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'suppliers/list.html', context)

@login_required
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'suppliers/detail.html', {'supplier': supplier})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier created successfully')
            return redirect('suppliers:list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/form.html', {'form': form, 'title': 'Create Supplier'})

@login_required
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier updated successfully')
            return redirect('suppliers:detail', pk=pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/form.html', {'form': form, 'supplier': supplier, 'title': 'Edit Supplier'})

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Supplier deleted successfully')
        return redirect('suppliers:list')
    return render(request, 'suppliers/confirm_delete.html', {'supplier': supplier})
