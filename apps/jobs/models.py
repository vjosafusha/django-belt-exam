from django.db import models
from ..users.models import User

class LocationManager(models.Manager):
    def easy_create(self, form):
        location = Location.objects.create(
            address = form['location']
        )
        return location.id

class Location(models.Model):
    address = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LocationManager()

class JobManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['title']) < 3:
            errors['title'] = "Job title must be longer than 3 characters"
        if len(form['description']) < 15:
            errors['description'] = "Description must be longer than 10 characters"
        if len(form['location']) < 1:
            errors['location'] = "Location must not be empty"
        return errors

    def easy_create(self, form, id, loc_id):
        user = User.objects.filter(id = id)
        location = Location.objects.filter(id = loc_id)
        Job.objects.create(
            title = form['title'],
            description = form['description'],
            creator = user[0],
            location = location[0]           
        )

    def job_join(self, user_id, job_id):
        user = User.objects.get(id = user_id)
        job = Job.objects.get(id = job_id)
        job.joined_by.add(user)
        job.save()
        

class Job(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name = 'jobs')
    joined_by = models.ManyToManyField(User, related_name = 'the_jobs')
    location = models.ForeignKey(Location, related_name = 'job_address')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    objects = JobManager()






