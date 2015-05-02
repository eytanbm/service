'''
Created on Apr 18, 2015

@author: eytan
'''
import django.utils.timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole


class TicketEevent(models.Model):
    
    ticket = models.ForeignKey(Ticket, related_name="events")
    timestamp = models.DateTimeField(default=django.utils.timezone.now())
    by = models.ForeignKey(TicketRole)

    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket Event")
        verbose_name_plural = _("Ticket Events")
        db_table = "ticket_event"

class TicketAttrChange(models.Model):
    
    event = models.ForeignKey(TicketEevent, related_name="atrributes")
    attr = models.CharField(max_length=40)
    value = models.CharField(max_length=120)

    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket Event Attribute Change")
        verbose_name_plural = _("Ticket Event Attribute Changes")
        db_table = "ticket_event_attribute"

    
