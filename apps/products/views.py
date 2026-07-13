from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'barcode', 'category', 'supplier',
                  'purchase_price', 'selling_price', 'cost_price', 'stock_quantity',
                  'minimum_stock', 'maximum_stock', 'location', 'image', 'status']

@login_required
def product_list(request):
    products = Product.objects.all()
    
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search) | products.filter(sku__icontains=search)
    
    context = {'products': products}
    return render(request, 'products/list.html', context)

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully')
            return redirect('products:list')
    else:
        form = ProductForm()
    return render(request, 'products/form.html', {'form': form, 'title': 'Create Product'})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('products:detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/form.html', {'form': form, 'product': product, 'title': 'Edit Product'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('products:list')
    return render(request, 'products/confirm_delete.html', {'product': product})
