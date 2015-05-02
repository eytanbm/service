'''
Created on Apr 25, 2015

@author: eytan
'''

from django.contrib.auth.models import User
from django.test.testcases import TestCase
from json import loads, dumps

from service_calls.api.serializers import TicketSerializer, \
    TicketDetailSerializer
from service_calls.content import TICKET_ROLE
from service_calls.content.models.content import Content
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole


class TestTicketSerializer(TestCase):
    
    def setUp(self):
        self.maxDiff=None
        self.serializer = TicketSerializer
        self.expected_data = {}      
        for indx in xrange(1000, 1004):
            Content.objects.create(
                                   id=indx,
                                   guest=Guest.objects.create(id=indx, first_name="guest%d" % indx, last_name="gutsy%d" % indx, room=indx),
                                   location=Location.objects.create(id=indx, other_location="Restaurant on %d floor" % indx),
                                   ticket=Ticket.objects.create(id=indx, owner=TicketRole.objects.create(id=indx, user=User.objects.create_user(username="user%d" % indx, password="xxxx")))
                                   )
            self.expected_data[indx] = {u'id': indx,u'owner': indx,u'priority': 2,u'source': 2,u'status': 1,u'type': 1,
                                        u'content': {u'guest': {u'id':indx, u'first_name':u'guest%d' % indx, u'last_name':u'gutsy%d' % indx, u'room':indx},
                                                     u'location':{u'id':indx, u'other_location': u'Restaurant on %d floor' % indx, u'room_number':None}, u'id':indx}
                                       }
                        
        
    def test_retrieve(self):
        queryset = Ticket.objects.all()
        serializer = TicketDetailSerializer(queryset, many=True)
        count = len(Ticket.objects.all())
        for indx in xrange(count):
            d = serializer.data[indx]
            id = d[u'id']
            serializer_data = loads(dumps(d))
            expected_data = self.expected_data[id]
            self.assertEqual(serializer_data, expected_data)
            
    def test_create(self):
        new_owner = TicketRole.objects.create(id=1005, user=User.objects.create_user(username="user1005", password="xxxx"))
        new_guest = Guest.objects.create(id=1005, first_name="guest101",last_name="gutsy101")
        new_location = Location.objects.create(id=1005, other_location="Restaurant on 101 floor")
        data = {
                "id":1005,
                "owner":new_owner.id
                ,
                "content":{"id":1005, "guest":new_guest.id, "location":new_location.id}
                }
        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid())
        ticket = serializer.save()
        self.assertEqual(ticket.content.guest.full_name, "guest101 gutsy101")
        self.assertEqual(ticket.content.location.other_location, "Restaurant on 101 floor")
        self.assertEqual(ticket.owner.role, TICKET_ROLE.Manager)
         
    def test_update(self):
        ticket = Ticket.objects.get(pk=1003)
        new_owner = owner=TicketRole.objects.create(user=User.objects.create_user(username="new_user1003", password="xxxx"))
        data = {"id":1003,"owner":new_owner.id, "content":{"id":ticket.content.id, "location":Location.objects.create(room_number=1111).id}}
        serializer = self.serializer(ticket, data=data)
        self.assertTrue(serializer.is_valid())
        updated_ticket = serializer.save()
        self.assertEqual(updated_ticket.owner.user.username, "new_user1003")
        self.assertEqual(updated_ticket.content.location.room_number, 1111)
        self.assertIsNone(updated_ticket.content.location.other_location)
         