'''
Created on May 9, 2015

@author: eytan
'''
from django.test.testcases import TestCase
import json
import random

from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole
from service_calls.utils.testing import LoginTestCase


class TestTicketComments(LoginTestCase):
    COMMENTS_COUNT = 100

    def setUp(self):
        LoginTestCase.setUp(self)
        ModelTestFixture()
        self.role = random.choice(TicketRole.objects.all())
        self.ticket = random.choice(Ticket.objects.all())        
    
    def test_add_comment(self):
        for i in xrange(self.COMMENTS_COUNT):
            response = self.client.post("/api/ticket/add_comment/", json.dumps({"ticket":self.ticket.id, "commentor": self.role.id, "text":"Bla bla %d" % i}), content_type="application/json")
            self.assertEqual(201, response.status_code)
            
        self.assertEqual(self.COMMENTS_COUNT, len(self.ticket.comments.all()))
        
        response = self.client.post("/api/ticket/comments/%d" % self.ticket.id, json.dumps({}), content_type="application/json")
        comments = json.loads(response.content)
        for c in comments:
            self.assertEqual(c["ticket"], self.ticket.id)
            self.assertEqual(c["commentor"], self.role.id)
            self.assertTrue("Bla bla" in c["text"])