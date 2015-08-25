'''
Created on Apr 24, 2015

@author: eytan
'''
import random

from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket import Ticket
from service_calls.models.ticket_role import TicketRole, TICKET_ROLE
from service_calls.utils.testing import AbstractModelTest
from service_calls.content import TICKET_ROLE_STATUS


class TestTicket(AbstractModelTest):
    
    def setUp(self):
        self.model = Ticket
        fixture = ModelTestFixture()
        owner = TicketRole.objects.get_or_create(user=fixture.users[0], role=TICKET_ROLE.Manager)[0]
        self.data = {"owner": owner, 'initiator': owner}
        self.update_data = {"owner": TicketRole.objects.get_or_create(user=fixture.users[1], role=TICKET_ROLE.Dispatcher)[0]}
        AbstractModelTest.setUp(self)
        
    def test(self):
        from_db = self.model.objects.get(pk=self.pk)
        self._assert_good_instance(from_db)
        self._update_instance(from_db)
        from_db = self.model.objects.get(pk=self.pk)
        self._assert_good_instance(from_db, data=self.update_data)
        self.assertEqual(from_db.status, TICKET_ROLE_STATUS[from_db.owner.role])
        