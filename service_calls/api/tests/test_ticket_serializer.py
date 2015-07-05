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
from service_calls.api.tests.create_ticket_fixture import CreateTicketFixture
from service_calls.api.tests.update_ticket_fixture import UpdateTicketFixture


class TestTicketSerializer(TestCase):
    
    def setUp(self):
        self.maxDiff=None
        self.serializer = TicketSerializer
        self.fixture = UpdateTicketFixture()
       
    def test_retrieve(self):
        queryset = Ticket.objects.all()
        serializer = TicketDetailSerializer(queryset, many=True)
        count = len(Ticket.objects.all())
        for indx in xrange(count):
            d = serializer.data[indx]
            id = d[u'id']
            d[u'created'] = d[u'created'].isoformat()
            d[u'updated'] = d[u'updated'].isoformat()
            serializer_data = loads(dumps(d))
            expected_data = self.fixture.expected_data[id]
            self.assertEqual(serializer_data, expected_data)
            
    def test_create(self):
        data = CreateTicketFixture().data
        serializer = self.serializer(data=data)
        self.assertTrue(serializer.is_valid())
        ticket = serializer.save()
        self.assertEqual(ticket.content.guest.full_name, "guest101 gutsy101")
        self.assertEqual(ticket.content.location.other_location, "Restaurant on 101 floor")
        self.assertEqual(ticket.owner.role, TICKET_ROLE.Manager)
         
    def test_update(self):
        serializer = self.serializer(self.fixture.ticket, data=self.fixture.data)
        self.assertTrue(serializer.is_valid())
        updated_ticket = serializer.save()
        self.assertEqual(updated_ticket.owner.user.username, "new_user1003")
        self.assertEqual(updated_ticket.content.location.room_number, 1111)
        self.assertIsNone(updated_ticket.content.location.other_location)
         