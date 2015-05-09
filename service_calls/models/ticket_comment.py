'''
Created on May 8, 2015

@author: eytan
'''
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
import pytz

from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole


class TicketComment(models.Model):
    
    ticket = models.ForeignKey(Ticket, related_name="comments")
    commentor = models.ForeignKey(TicketRole, null=True, blank=True, related_name="comments")
    timestamp = models.DateTimeField(default=pytz.utc.localize(datetime.now()))
    text = models.TextField()
    
    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket Comment")
        verbose_name_plural = _("Ticket Comments")
        db_table = "ticket_comment"
