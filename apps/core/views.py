from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match')
        
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        
        return cleaned_data

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    return render(request, 'core/landing.html')

@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'core/login.html')

@require_http_methods(['GET', 'POST'])
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('core:login')
    else:
        form = RegisterForm()
    
    return render(request, 'core/register.html', {'form': form})

@require_http_methods(['POST'])
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('core:landing')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            messages.info(request, 'Password reset link has been sent to your email')
        except User.DoesNotExist:
            messages.info(request, 'If an account exists with this email, a reset link has been sent')
    
    return render(request, 'core/forgot_password.html')
