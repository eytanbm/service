'''
Created on Apr 29, 2015

@author: eytan
'''
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from service_calls.api.views import TicketList, create_ticket, update_ticket,\
    TicketHistory, load_faults


urlpatterns = patterns('service_calls.content.views',
    url(r'^tickets/$', login_required(TicketList.as_view()), name='tickets_list'),
    url(r'^ticket/create/$', login_required(create_ticket), name='tickets_list'),
    url(r'^ticket/update/(?P<pk>[0-9]+)$', login_required(update_ticket), name='tickets_list'),
    url(r'^ticket/history/(?P<pk>[0-9]+)$', login_required(TicketHistory.as_view()), name='ticket_history'),   
    url(r'^faults/load$', login_required(load_faults), name='load_faults'),
    )
