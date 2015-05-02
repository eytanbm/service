'''
Created on Apr 25, 2015

@author: eytan
'''

import random

from service_calls.content.models.content import Content
from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.models.tests.fixture import ModelTestFixture
from service_calls.models.ticket import Ticket
from service_calls.utils.testing import AbstractModelTest


class TestContent(AbstractModelTest):
    def setUp(self):
        self.model = Content
        ModelTestFixture()
        guest = Guest.objects.create(first_name="John", last_name="Smith")
        location = Location.objects.create(room_number=1134)
        self.data = {"guest":guest, "location":location, "ticket":random.choice(Ticket.objects.all())}
        self.update_data = {"location":Location.objects.create(room_number=1124)}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
