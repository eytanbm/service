'''
Created on Nov 27, 2013

@author: eytan
'''
from django.test import TestCase

from  django.utils.translation import ugettext_lazy as _
from service_calls.utils import Enumeration

class TestEnumeration(TestCase):
    
    def test(self):
        enum = Enumeration('A', 'B', 'C')
        
        self.assertEquals(1, enum.A)
        self.assertEquals(2, enum.B)
        self.assertEquals(3, enum.C)
        
        self.assertEquals(((1,'A'),(2,'B'),(3,'C'),), enum.to_choices())
        
        self.assertEquals(enum.B, enum.after(enum.A))
        self.assertEquals(enum.C, enum.after(enum.B))
        self.assertEquals(enum.B, enum.before(enum.C))
        self.assertEquals(enum.A, enum.before(enum.B))
        
        self.assertIsNone(enum.before(enum.A))
        self.assertIsNone(enum.after(enum.C))
        
        self.assertEquals('A', enum.name(enum.A))
        self.assertEquals('A', enum.name(1))
        self.assertIsNone(enum.name(5))
        try:
            enum['x'] = 'x'
            self.fail("should throw exception!")
        except Exception as expected:
            self.assertEquals("Enumeration is immutable!", str(expected))
        try:
            del enum.A
            self.fail("should throw exception!")
        except Exception as expected:
            self.assertEquals("Enumeration is immutable!", str(expected))
            
        
    def test_with_display_name(self):
        enum = Enumeration((u'A', _(u'Aye')), (u'B', _(u'Bye')), u'C')
        
        self.assertEquals(1, enum.A)
        self.assertEquals(2, enum.B)
        self.assertEquals(3, enum.C)
        
        self.assertEquals(((1,'Aye'),(2,'Bye'),(3,'C'),), enum.to_choices())
        
        self.assertEquals(enum.B, enum.after(enum.A))
        self.assertEquals(enum.C, enum.after(enum.B))
        self.assertEquals(enum.B, enum.before(enum.C))
        self.assertEquals(enum.A, enum.before(enum.B))
        
        self.assertIsNone(enum.before(enum.A))
        self.assertIsNone(enum.after(enum.C))
        
        self.assertEquals('A', enum.name(enum.A))
        self.assertEquals('A', enum.name(1))
        self.assertIsNone(enum.name(5))
        try:
            enum['x'] = 'x'
            self.fail("should throw exception!")
        except Exception as expected:
            self.assertEquals("Enumeration is immutable!", str(expected))
        try:
            del enum.A
            self.fail("should throw exception!")
        except Exception as expected:
            self.assertEquals("Enumeration is immutable!", str(expected))
            
        
        