'''
Created on Apr 24, 2015

@author: eytan
'''
from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole, TICKET_ROLE
from service_calls.utils.testing import AbstractModelTest


class TestTicket(AbstractModelTest):
    
    def setUp(self):
        self.model = Ticket
        fixture = ModelTestFixture()
        self.data = {"owner": TicketRole.objects.get_or_create(user=fixture.users[0], role=TICKET_ROLE.Manager)[0]}
        self.update_data = {"owner": TicketRole.objects.create(user=fixture.users[1], role=TICKET_ROLE.Dispatcher)}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()