from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.read, name = 'all'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^show/(?P<id>\d+)$', views.show, name = 'show'),
    url(r'^edit/(?P<job_id>\d+)$', views.edit, name = 'edit'),
    url(r'^update$', views.update, name = 'update'),
    url(r'^join/(?P<job_id>\d+)$', views.join, name = 'join'),
    url(r'^cancel/(?P<job_id>\d+)$', views.cancel, name = 'cancel')

]