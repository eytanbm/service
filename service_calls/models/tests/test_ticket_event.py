'''
Created on Apr 25, 2015

@author: eytan
'''
import random

from service_calls.content import TICKET_ROLE, TICKET_STATUS
from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket_event import TicketAttrChange, TicketEevent
from service_calls.models.ticket_role import TicketRole
from service_calls.utils.testing import AbstractModelTest


class TestTicketEvent(AbstractModelTest):
    
    def setUp(self):
        self.model = TicketEevent
        fixture = ModelTestFixture()
        ticket = fixture.random_ticket()
        self.data = {"ticket":ticket, "by":ticket.owner}
        self.update_data = {"by":fixture.random_role()}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()

class TestTicketAttrChange(AbstractModelTest):
    
    def setUp(self):
        self.model = TicketAttrChange
        fixture = ModelTestFixture()
        event = TicketEevent.objects.create(ticket=fixture.random_ticket(), by=fixture.random_role())
        self.data = {"event":event, "attr":"status", "value":str(TICKET_STATUS.Done)}
        self.update_data = {"value":str(TICKET_STATUS.Closed)}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
