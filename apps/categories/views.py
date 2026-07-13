from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']

@login_required
def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories/list.html', context)

@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully')
            return redirect('categories:list')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form, 'title': 'Create Category'})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('categories:detail', pk=pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/form.html', {'form': form, 'category': category, 'title': 'Edit Category'})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully')
        return redirect('categories:list')
    return render(request, 'categories/confirm_delete.html', {'category': category})
