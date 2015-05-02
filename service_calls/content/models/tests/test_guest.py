'''
Created on Apr 25, 2015

@author: eytan
'''
from service_calls.utils.testing import AbstractModelTest
from service_calls.content.models.guest import Guest

class TestGuest(AbstractModelTest):
    def setUp(self):
        self.model = Guest
        self.data = {"first_name": "John", "last_name":"Smith"}
        self.update_data = {"first_name": "Johnny"}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()    