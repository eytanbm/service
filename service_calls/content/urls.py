'''
Created on Apr 29, 2015

@author: eytan
'''
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from service_calls.content.views import load_guests, load_locations, \
    get_static_content, load_faults, locations, LocationList, GuestList,\
    FaultList


urlpatterns = patterns('service_calls.content.views',
    url(r'^guests/load/$', login_required(load_guests), name='load_guests'),
    url(r'^guests/$', login_required(GuestList.as_view()), name='load_guests'),
    url(r'^locations/load/$', login_required(load_locations), name='load_locations'),
    url(r'^locations/$', login_required(LocationList.as_view()), name='locations'),
    url(r'^faults/load/$', login_required(load_faults), name='load_faults'),
    url(r'^faults/$', login_required(FaultList.as_view()), name='load_faults'),
    url(r'^static/$', login_required(get_static_content), name='get_static'),
    )