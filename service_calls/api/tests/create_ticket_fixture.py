'''
Created on May 2, 2015

@author: eytan
'''
from django.contrib.auth.models import User

from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.models.ticket_role import TicketRole
from service_calls.content import TICKET_ROLE


class CreateTicketFixture(object):
    def __init__(self):
        new_owner = TicketRole.objects.create(id=1005, role=TICKET_ROLE.Manager, user=User.objects.create_user(username="user1005", password="xxxx"))
        new_guest = Guest.objects.create(id=1005, first_name="guest101",last_name="gutsy101")
        new_location = Location.objects.create(id=1005, other_location="Restaurant on 101 floor")
        self.data = {
#                 "id":1005,
                "owner":new_owner.id,
                "initiator":new_owner.id,
                "content":{"id":1005, "guest":new_guest.id, "location":new_location.id}
                }

