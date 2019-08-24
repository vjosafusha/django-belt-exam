from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name'])<2:
            errors['first_name'] = 'First name must be longer than two characters'
        elif form['first_name'].isalpha() == False:
            errors['first_name'] = 'First name cannot contain numbers or special characters!'
        if len(form['last_name'])<2:
            errors['last_name'] = 'Last name should be longer than two characters'
        elif form['last_name'].isalpha() == False:
            errors['last_name'] = 'Last name cannot contain numbers or special characters!'
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Email not valid'
        if len(form['password']) < 8:
            errors['password'] = 'Password must be longer than eight characters!'
        if form['password'] != form['conf_password']:
            errors['not_a_match'] = 'Passwords must match!'
        return errors

    def easy_create(self, form):
        hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            pw_hash = hashed_pw
        )
        return user.id

    def login(self, form):
        existing_user = User.objects.filter(email = form['email'])
        if existing_user:
            user = existing_user[0]
            bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode())
            return(True, user.id)
        return(False, 'Email or password invalid')

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    pw_hash = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
