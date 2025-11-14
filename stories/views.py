from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm
from .models import Story

def index(request):
    
    stories = Story.objects.all()
    return render(request, 'stories/index.html', {'stories': stories})

def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to You VS HR.')
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'stories/register.html', {'form': form})

def user_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('index')
    else:
        form = AuthenticationForm()
    
   
    for field in form.fields:
        form.fields[field].widget.attrs.update({'class': 'form-control'})
    
    return render(request, 'stories/login.html', {'form': form})

def user_logout(request):
    
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')