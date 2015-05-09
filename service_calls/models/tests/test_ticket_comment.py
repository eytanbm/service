'''
Created on May 9, 2015

@author: eytan
'''
import random

from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_comment import TicketComment
from service_calls.models.ticket_role import TicketRole
from service_calls.utils.testing import AbstractModelTest


class TestTicketComment(AbstractModelTest):
    
    def setUp(self):
        ModelTestFixture()
        self.model = TicketComment
        self.data = {"ticket":random.choice(Ticket.objects.all()), "commentor":random.choice(TicketRole.objects.all()), "text":"Bla bla"}
        self.update_data = {"text":"Bla bla and bla"}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
    