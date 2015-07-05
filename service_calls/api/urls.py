'''
Created on Apr 29, 2015

@author: eytan
'''
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.decorators.csrf import csrf_exempt

from service_calls.api.views import TicketList, TicketHistory, \
    CreateTicketView, UpdateTicketView, ticket_comments, AddTicketComment, \
    user_info, role_info


def secure_func(func):
    return login_required(func)

urlpatterns = patterns('service_calls.content.views',
    url(r'^tickets/$', secure_func(TicketList.as_view()), name='tickets_list'),
    url(r'^ticket/create/$', secure_func(CreateTicketView.as_view()), name='tickets_create'),
    url(r'^ticket/update/(?P<pk>[0-9]+)$', secure_func(UpdateTicketView.as_view()), name='ticket_update'),   
    url(r'^ticket/history/(?P<pk>[0-9]+)$', secure_func(TicketHistory.as_view()), name='ticket_history'),   
    url(r'^ticket/add_comment/$', secure_func(AddTicketComment.as_view()), name='ticket_add_comment'),   
    url(r'^ticket/comments/(?P<pk>[0-9]+)$', secure_func(ticket_comments), name='ticket_comments'),   
    url(r'^login/$', csrf_exempt(login), {'template_name': 'login.html'}),   
    url(r'^logout/$', logout),   
    url(r'^user/(?P<username>\w+)$', csrf_exempt(user_info), name='user_info'),   
    url(r'^role/(?P<role_id>[0-9]+)$', csrf_exempt(role_info), name='role_name'),   
    )
