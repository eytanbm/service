'''
Created on Apr 24, 2015

@author: eytan
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _
from service_calls.models.ticket import Ticket

class Location(models.Model):
    
    room_number = models.IntegerField(null=True, blank=True)
    other_location = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        app_label = "content"
        verbose_name = _("Location")
        verbose_name_plural = _('Locations')
        db_table = "location"
        
    def __unicode__(self):
        return u'Room: %d' % self.room_number if self.room_number else self.other_location if self.other_location else u'Unknown'
    