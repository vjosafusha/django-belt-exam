from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.all_jobs, name = 'all_jobs'),
    url(r'^add_job$', views.add_job, name = 'add_job'),
    url(r'^create_job$', views.create_job, name = 'create_job'),
    url(r'^show/(?P<id>\d+)$', views.show_job, name = 'show_job'),
    url(r'^join/(?P<job_id>\d+)$', views.join_job, name = 'join_job'),
    url(r'^edit/(?P<job_id>\d+)$', views.edit_job, name = 'edit_job'),
    url(r'^cancel/(?P<job_id>\d+)$', views.cancel, name = 'cancel'),
    url(r'^update$', views.update, name = 'update'),
]