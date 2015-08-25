'''
Created on Oct 11, 2014

@author: eytan
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _

from service_calls.models.ticket import Ticket


FILES_ROOT = "files/tickets/"

def file_path(self, filename):
    url = "%s/%s/%s" % (FILES_ROOT, self.ticket.id, filename)
    return url

class TicketFile(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="files")
    file = models.FileField(upload_to=file_path)

    class Meta:
        app_label = 'service_calls'
        verbose_name = _('File')
        verbose_name_plural = _('Files')
        db_table = "file"
