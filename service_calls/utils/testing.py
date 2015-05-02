'''
Created on Apr 25, 2015

@author: eytan
'''

from django.contrib.auth.models import User
from django.test.testcases import TestCase


class AbstractModelTest(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.pk = self.model.objects.create(**self.data).pk
        
    def _assert_good_instance(self, instnance, data=None):
        if not data:
            data = self.data
        for k in data.keys():
            self.assertEqual(data[k], getattr(instnance, k), "<%s expected='%s'>Actual<'%s'>" % (k, str(data[k]), str(getattr(instnance, k))))
            
    def _update_instance(self, instance, data=None):
        if not data:
            data = self.update_data
        for k in data.keys():
            setattr(instance, k, data[k])
        instance.save()
        
    def _test(self):
        from_db = self.model.objects.get(pk=self.pk)
        self._assert_good_instance(from_db)
        self._update_instance(from_db)
        from_db = self.model.objects.get(pk=self.pk)
        self._assert_good_instance(from_db, data=self.update_data)

class ABstractDBEnumerationTestCase(AbstractModelTest):
        
    def setUp(self):
        self.data = {"value":5, "name":"Test name"}
        self.update_data = {"name":"New Test name"}
        AbstractModelTest.setUp(self)      
        
    def _enum_test(self):
        self._test()
        self.assertEqual(0, self.model.objects.default.pk)
        self.assertEqual(self.model.default_name, self.model.objects.default.name)
        
class LoginTestCase(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        User.objects.create_superuser('eytan', 'a@x.com', 'test')
        login_successful = self.client.login(username="eytan",password="test")
        self.assertTrue(login_successful)


