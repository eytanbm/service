'''
Created on Apr 18, 2015

@author: eytan
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _

from service_calls.models.ticket_role import TicketRole
from service_calls.content import TICKET_TYPE, TICKET_PRIORITY, TICKET_STATUS,\
    TICKET_SOURCE

class Ticket(models.Model):

    type = models.IntegerField(choices=TICKET_TYPE.to_choices(), default=TICKET_TYPE.Problem)
    source = models.IntegerField(choices=TICKET_SOURCE.to_choices(), default=TICKET_SOURCE.Maintenance)
    priority = models.IntegerField(choices=TICKET_PRIORITY.to_choices(), default=TICKET_PRIORITY.Normal)    
    status = models.IntegerField(choices=TICKET_STATUS.to_choices(), default=TICKET_STATUS.Reported)  
    owner = models.ForeignKey(TicketRole, null=True, blank=True, related_name="tickets")
    
    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket")
        verbose_name_plural = _('Tickets')
        db_table = "ticket"
        
    @property
    def prior(self):
        return TICKET_PRIORITY.name(self.priority)
    @property
    def typ(self):
        return TICKET_TYPE.name(self.type)
    @property
    def src(self):
        return TICKET_SOURCE.name(self.source)
    @property
    def sta(self):
        return TICKET_STATUS.name(self.status)
    @property
    def location(self):
        try:
            return self.content.location
        except:
            return  u'Unknown'
    
    def __unicode__(self):
        return u'[%s]%s[%s]-%s' %(self.src, self.typ, self.sta, self.location)


