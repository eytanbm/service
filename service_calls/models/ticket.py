'''
Created on Apr 18, 2015

@author: eytan
'''
from datetime import datetime
from django.db import models
from django.db.transaction import atomic
from django.utils.translation import ugettext_lazy as _
import pytz

from service_calls.content import TICKET_TYPE, TICKET_PRIORITY, TICKET_STATUS, \
    TICKET_SOURCE, TICKET_DEPARTMENT, TICKET_ROLE_STATUS
from service_calls.models.ticket_role import TicketRole
from service_calls.utils.track_changes import track_changes


@track_changes('priority', 'status', 'owner')
class Ticket(models.Model):

    type = models.IntegerField(choices=TICKET_TYPE.to_choices(), default=TICKET_TYPE.Problem)
    source = models.IntegerField(choices=TICKET_SOURCE.to_choices(), default=TICKET_SOURCE.Maintenance)
    priority = models.IntegerField(choices=TICKET_PRIORITY.to_choices(), default=TICKET_PRIORITY.Normal)    
    status = models.IntegerField(choices=TICKET_STATUS.to_choices(), default=TICKET_STATUS.Created)  
    owner = models.ForeignKey(TicketRole, null=True, blank=True, related_name="tickets")
    initiator = models.ForeignKey(TicketRole, null=False, blank=False, related_name="initiated_tickets")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    planned_start = models.DateTimeField(null=True, blank=True)
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)
    
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
    
    @property
    def department(self):
        return TICKET_DEPARTMENT.name(self.owner.department)
    
    def __setattr__(self, name, value):
        super(Ticket, self).__setattr__(name, value)
        if name == 'owner_id' and value:
            super(Ticket, self).__setattr__('status', TICKET_STATUS.Assigned)
        if name == 'owner_id' and value is None:
            super(Ticket, self).__setattr__('status', TICKET_STATUS.Created)
    
    def _save_change_event(self):
        changes = self.whats_changed()
        if changes:
            from service_calls.models.ticket_event import TicketEvent, TicketAttrChange
            updator = None
            try:
                updator = self.updated_by
            except AttributeError:
                pass
#             print changes
            event = TicketEvent.objects.create(ticket=self, timestamp = pytz.utc.localize(datetime.now()), by=updator)
            changes = self.whats_changed()
            for k in changes:
                TicketAttrChange.objects.create(event=event, attr=k, from_value=str(changes[k]), to_value=str(getattr(self, k)))
    
    @atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self._save_change_event()
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


