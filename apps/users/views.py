from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'users/index.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('users:index')
    user_id = User.objects.easy_create(request.POST)
    print(user_id)
    request.session['user_id'] = user_id    
    return redirect ('jobs:all_jobs')

def login(request):
    valid, result = User.objects.login(request.POST)
    if not valid:
        messages.error(request, result)
        return redirect('users:index')
    request.session['user_id'] = result
    return redirect('jobs:all_jobs')

def logout(request):
    request.session.clear()
    return redirect('users:index')

