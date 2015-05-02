'''
Created on May 2, 2015

@author: eytan
'''
import json
import os

from service_calls.api.tests.create_ticket_fixture import CreateTicketFixture
from service_calls.api.tests.update_ticket_fixture import UpdateTicketFixture
from service_calls.utils.testing import LoginTestCase
from service_calls.models.ticket import Ticket


class TestCreateTicket(LoginTestCase):
     
    def setUp(self):
        super(TestCreateTicket, self).setUp()
        self.fixture = CreateTicketFixture()
             
    def test(self):
        response = self.client.post("/api/ticket/create/", json.dumps(self.fixture.data), content_type="application/json")
        self.assertEqual(200, response.status_code)
        
class TestUpdateTicket(LoginTestCase):
    def setUp(self):
        super(TestUpdateTicket, self).setUp()
        self.fixture = UpdateTicketFixture()
        
    def test(self):
        pk = self.fixture.ticket.id
        response = self.client.post("/api/ticket/update/%d" % pk, json.dumps(self.fixture.data), content_type="application/json")
        self.assertEqual(200, response.status_code)
        updated_ticket = Ticket.objects.get(pk=pk)
        self.assertEqual(updated_ticket.owner.user.username, "new_user1003")
        self.assertEqual(updated_ticket.content.location.room_number, 1111)
        self.assertIsNone(updated_ticket.content.location.other_location)
             

            
