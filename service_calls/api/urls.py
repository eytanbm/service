'''
Created on Apr 29, 2015

@author: eytan
'''
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from service_calls.api.views import TicketList


urlpatterns = patterns('service_calls.content.views',
    url(r'^tickets/', login_required(TicketList.as_view()), name='tickets_list'),
    )
