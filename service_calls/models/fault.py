'''
Created on May 6, 2015

@author: eytan
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Fault(models.Model):

    name = models.CharField(max_length=250, unique=True)
        
    class Meta:
        app_label = "service_calls"
        verbose_name = _("Fault")
        verbose_name_plural = _('Faults')
        db_table = "fault"
        
    def __unicode__(self):
        return u'%s' % self.name
