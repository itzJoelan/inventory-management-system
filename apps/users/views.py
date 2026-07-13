from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

@login_required
def user_profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'User updated successfully')
        return redirect('users:profile')
    return render(request, 'users/edit.html', {'user': user})
