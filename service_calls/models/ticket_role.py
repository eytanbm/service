'''
Created on Apr 23, 2015

@author: eytan
'''
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from service_calls.utils.enumeration import Enumeration
from service_calls.content import TICKET_ROLE


class TicketRoleManager(models.Manager):
    
    def has_role(self, role, user):
        return self.get(role=role, user=user).exists()
    
    def add_role(self, role, user):
        return self.get_or_create(user=user, role=role)[0]

    def remove_role(self, role, user):
        try:
            self.get(user=user, role=role).delete()
        except TicketRole.DoesNotExist:
            pass

class TicketRole(models.Model):
    
    user = models.ForeignKey(User, related_name="ticket_roles")
    role = models.IntegerField(choices=TICKET_ROLE.to_choices(), default=TICKET_ROLE.Manager)
    
    objects = TicketRoleManager()
    
    class Meta:
        app_label = "service_calls"
        verbose_name = _("Ticket Role")
        verbose_name_plural = _("Ticket Roles")
        db_table = "ticket_role"
        unique_together = (("user", "role"),)

    def __unicode__(self):
        return u'%s(%s)' % (TICKET_ROLE.name(self.role), self.user.username)