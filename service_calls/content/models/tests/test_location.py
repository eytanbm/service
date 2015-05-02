'''
Created on Apr 25, 2015

@author: eytan
'''
from service_calls.content.models.location import Location
from service_calls.utils.testing import AbstractModelTest


class TestLocationWithRoomNumber(AbstractModelTest):
    def setUp(self):
        self.model = Location
        self.data = {"room_number":1134}
        self.update_data = {"room_number": 1124}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
        
class TestLocationWithOtherLocation(AbstractModelTest):
    def setUp(self):
        self.model = Location
        self.data = {"other_location":"Restaurant on 2nd floor"}
        self.update_data = {"other_location": "Restaurant on 3rd floor"}
        AbstractModelTest.setUp(self)
        
    def test(self):
        self._test()
        
   