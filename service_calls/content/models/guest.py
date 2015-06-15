'''
Created on Apr 24, 2015

@author: eytan
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _
from service_calls.content.models.location import Location

class Guest(models.Model):
    
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    room = models.IntegerField(null=True, blank=True)
    arrival = models.DateTimeField(null=True, blank=True)
    departure = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        app_label = "content"
        verbose_name = _("Guest")
        verbose_name_plural = _('Guests')
        db_table = "guest"
        
    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def __unicode__(self):
        return u'Guest: %s' % self.full_name
