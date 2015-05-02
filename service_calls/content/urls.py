'''
Created on Apr 29, 2015

@author: eytan
'''
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from service_calls.content.views import load_guests, load_locations


urlpatterns = patterns('service_calls.content.views',
    url(r'^guests/load$', login_required(load_guests), name='load_guests'),
    url(r'^locations/load$', login_required(load_locations), name='load_locations'),
    )