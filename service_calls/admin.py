'''
Created on May 2, 2015

@author: eytan
'''
from django.contrib import admin

from service_calls.content.models.content import Content
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.content.models.fault import Fault
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole
from service_calls.models.ticket_comment import TicketComment


admin.site.register(Guest)
admin.site.register(Location)
admin.site.register(Fault)
class ContentAdmin(admin.TabularInline):
    model=Content
    fk_name = "ticket"
    
admin.site.register(TicketRole)
class TicketAdmin(admin.ModelAdmin):
    inlines = [
               ContentAdmin,
               ]  
admin.site.register(Ticket,TicketAdmin)

admin.site.register(TicketComment)