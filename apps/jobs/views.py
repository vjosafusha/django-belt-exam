from django.shortcuts import render, redirect
from django.contrib import messages
from ..users.models import User
from .models import Job, Location

def all_jobs(request):
    if 'user_id' not in request.session:
        return redirect('users:index')
    context = {
        'user_by_id': User.objects.get(id = request.session['user_id']),
        'all_jobs': Job.objects.exclude(seekers = request.session['user_id']),
        'my_jobs': Job.objects.filter(seekers = request.session['user_id'])
    }
    return render(request, 'jobs/main.html', context)

def add_job(request):
    return render(request, 'jobs/new.html')

def create_job(request):
    errors = Job.objects.validate(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('jobs:add_job')
    else:
        loc_id = Location.objects.easy_create(request.POST)
        Job.objects.easy_create(request.POST, request.session['user_id'], loc_id)
    return redirect('jobs:all_jobs')

def show_job(request, id):
    context = {
        'job_by_id': Job.objects.get(id=id),
    }
    return render(request, 'jobs/show.html',context)

def join_job(request, job_id):
    Job.objects.job_join(request.session['user_id'], job_id)
    return redirect('jobs:all_jobs')

def edit_job(request, job_id):
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
        return redirect('jobs:edit_job')
    else:
        job = Job.objects.get(id = job_id)
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.location.address = request.POST['location']
        job.save()
    return redirect('jobs:all_jobs')

def cancel(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('jobs:all_jobs')

