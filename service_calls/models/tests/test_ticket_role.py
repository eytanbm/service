'''
Created on Apr 23, 2015

@author: eytan
'''
from django.contrib.auth.models import User

from service_calls.models.ticket_role import TicketRole
from service_calls.utils.testing import AbstractModelTest
from service_calls.content import TICKET_ROLE


class TestTicketRole(AbstractModelTest):
    
    def setUp(self):
        self.model = TicketRole
        self.data = {"role":TICKET_ROLE.Manager, "user":User.objects.create_user("test_user", password="test_user")}
        self.update_data = {"role":TICKET_ROLE.Assignee}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
        