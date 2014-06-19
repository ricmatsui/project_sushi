from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('projects.urls', namespace='projects', app_name='projects')),

    url(r'^admin/', include(admin.site.urls)),
)