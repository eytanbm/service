'''
Created on Apr 25, 2015

@author: eytan
'''
import random

from service_calls.content import TICKET_ROLE, TICKET_STATUS
from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket_event import  TicketEvent, TicketAttrChange
from service_calls.models.ticket_role import TicketRole
from service_calls.utils.testing import AbstractModelTest


class TestTicketEvent(AbstractModelTest):
    
    def setUp(self):
        self.model = TicketEvent
        fixture = ModelTestFixture()
        ticket = fixture.random_ticket()
        self.data = {"ticket":ticket, "by":ticket.owner.user}
        self.update_data = {"by":fixture.random_role().user}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()

class TestTicketAttrChange(AbstractModelTest):
    
    def setUp(self):
        self.model = TicketAttrChange
        fixture = ModelTestFixture()
        event = TicketEvent.objects.create(ticket=fixture.random_ticket(), by=fixture.random_role().user)
        self.data = {"event":event, "attr":"status", "from_value":str(TICKET_STATUS.Done)}
        self.update_data = {"to_value":str(TICKET_STATUS.Closed)}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
