'''
Created on May 6, 2015

@author: eytan
'''
from django.contrib.auth.models import User

from service_calls.models.ticket_role import TicketRole
from service_calls.utils.testing import AbstractModelTest
from service_calls.content import TICKET_ROLE
from service_calls.content.models.fault import Fault


class TestTicketRole(AbstractModelTest):
    
    def setUp(self):
        self.model = Fault
        self.data = {"name":"Fault for test"}
        self.update_data = {"name":"New fault for test"}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()