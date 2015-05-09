'''
Created on Apr 25, 2015

@author: eytan
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _

from service_calls.content.models.fault import Fault
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.models.ticket import Ticket


class Content(models.Model):
    
    ticket = models.OneToOneField(Ticket, null=True, blank=True, related_name="content")
    location = models.ForeignKey(Location, null=True, blank=True, related_name="content")
    guest = models.ForeignKey(Guest, null=True, blank=True, related_name="content")
    fault = models.ForeignKey(Fault, null=True, blank=True, related_name="content")
    
    class Meta:
        app_label = "content"
        verbose_name = _("Content")
        verbose_name_plural = _('Contents')
        db_table = "content"
    