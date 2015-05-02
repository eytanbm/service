'''
Created on Apr 29, 2015

@author: eytan
'''
from django.contrib.auth.models import User
from django.test.client import Client
from django.test.testcases import TestCase
import json
import os

from service_calls.content.models.guest import Guest
from service_calls.content.models.location import Location
from service_calls.settings import BASE_DIR
from service_calls.utils.testing import LoginTestCase


class TestLoadGuests(LoginTestCase):
    
    def setUp(self):
        super(TestLoadGuests, self).setUp()
        with open(os.path.join(BASE_DIR, "service_calls/content/data", "guests.json")) as data_file:
            self.data = json.load(data_file)

            
    def test(self):
        response = self.client.post("/content/guests/load", json.dumps(self.data), content_type="application/json")
        self.assertEqual(len(self.data), len(Guest.objects.all()))
        for d in self.data:
            self.assertTrue(Guest.objects.filter(**d).exists())
            
class TestLoadLocations(LoginTestCase):
    
    def setUp(self):
        super(TestLoadLocations, self).setUp()
        self.data = []
        for floor in xrange(1,6):
            for room in xrange(1,22):
                self.data.append({"room_number":int("%d%003d" % (floor, room))})
            self.data.append({"other_location":"Laundry room floor: %d" % floor})
    def test(self):
        self.client.post("/content/locations/load", json.dumps(self.data), content_type="application/json")
        self.assertEqual(len(self.data), len(Location.objects.all()))
        for d in self.data:
            self.assertTrue(Location.objects.filter(**d).exists())
    
            
        
        