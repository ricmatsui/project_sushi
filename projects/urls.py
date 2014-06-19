from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('projects.views',
    url(r'^$', 'index')
)