'''
Created on May 2, 2015

@author: eytan
'''
from django.contrib.auth.models import User

from service_calls.content.models.content import Content
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole
from service_calls.content.models.fault import Fault


class UpdateTicketFixture(object):
    def __init__(self):
        self.expected_data = {}      
        for indx in xrange(1000, 1004):
            owner = TicketRole.objects.create(id=indx, user=User.objects.create_user(username="user%d" % indx, password="xxxx"))
            ticket = Ticket.objects.create(id=indx, 
                owner=owner, 
                initiator=owner)
            Content.objects.create(
                                   id=indx,
                                   guest=Guest.objects.create(id=indx, first_name="guest%d" % indx, last_name="gutsy%d" % indx, room=indx),
                                   location=Location.objects.create(id=indx, other_location="Restaurant on %d floor" % indx),
                                   ticket=ticket
                                   )
            self.expected_data[indx] = {u'id': indx,u'owner': indx,u'initiator':indx, u'priority': 2,u'source': 2,u'status': 1,u'type': 1,\
                                        u'created':ticket.created.isoformat(),\
                                        u'updated':ticket.updated.isoformat(),\
                                        u'planned_start':None,\
                                        u'actual_start':None,\
                                        u'actual_end':None,\
                                        u'content': {u'guest': {u'id':indx, u'first_name':u'guest%d' % indx, u'last_name':u'gutsy%d' % indx, u'room':indx, u'arrival':None, u'departure':None},
                                                     u'location':{u'id':indx, u'other_location': u'Restaurant on %d floor' % indx, u'room_number':None}, u'id':indx,\
                                                     }
                                       }
        self.ticket = Ticket.objects.get(pk=1003)
        new_owner = owner=TicketRole.objects.create(user=User.objects.create_user(username="new_user1003", password="xxxx"))
        self.data = {"id":1003,"owner":new_owner.id, "initiator":new_owner.id, "content":{"id":self.ticket.content.id, "location":Location.objects.create(room_number=1111).id}}
            
