'''
Created on Apr 18, 2015

@author: eytan
'''
from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone
from django.utils.translation import ugettext_lazy as _

from service_calls.models.ticket import Ticket


class TicketEvent(models.Model):
    
    ticket = models.ForeignKey(Ticket, related_name="history")
    timestamp = models.DateTimeField(default=django.utils.timezone.now())
    by = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket Event")
        verbose_name_plural = _("Ticket Events")
        db_table = "ticket_event"

class TicketAttrChange(models.Model):
    
    event = models.ForeignKey(TicketEvent, related_name="atrributes")
    attr = models.CharField(max_length=40)
    from_value = models.CharField(max_length=120, default="None")
    to_value = models.CharField(max_length=120, default="None")

    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket Event Attribute Change")
        verbose_name_plural = _("Ticket Event Attribute Changes")
        db_table = "ticket_event_attribute"

    
