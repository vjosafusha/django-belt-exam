from django.shortcuts import render, redirect
from django.contrib import messages
from ..users.models import User
from .models import Job, Location

def read(request):
    if 'user_id' not in request.session:
        return redirect('users:index')
    context = {
        'user_by_id': User.objects.get(id = request.session['user_id']),
        'all_jobs': Job.objects.exclude(joined_by = request.session['user_id']),
        'my_jobs': Job.objects.filter(joined_by = request.session['user_id'])
    }
    return render(request, 'jobs/main.html', context)

def add(request):
    return render(request, 'jobs/new.html')

def create(request):
    errors = Job.objects.validate(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('jobs:add')
    else:
        loc_id = Location.objects.easy_create(request.POST)
        Job.objects.easy_create(request.POST, request.session['user_id'], loc_id)
    return redirect('jobs:all')

def edit(request, job_id):
    context = {
        'job_by_id': Job.objects.get(id=job_id),
    }
    return render(request, 'jobs/edit.html', context)

def update(request):
    errors = Job.objects.validate(request.POST)
    job_id = request.POST['job_id']
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('jobs:edit', job_id = job_id)
    else:
        job = Job.objects.get(id = job_id)
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.location.address = request.POST['location']
        job.save()
    return redirect('jobs:all')

def show(request, id):
    context = {
        'job_by_id': Job.objects.get(id=id),
    }
    return render(request, 'jobs/show.html',context)

def join(request, job_id):
    Job.objects.job_join(request.session['user_id'], job_id)
    return redirect('jobs:all')

def cancel(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('jobs:all')

