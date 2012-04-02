import unittest
from django.test.client import Client
from django.test.utils import override_settings
from .models import TestModel

class VisitObjectTest(unittest.TestCase):
    def setUp(self):
        self.c = Client()
        self.test1 = TestModel()
        self.test1.save()
        self.test2 = TestModel()
        self.test2.save()

    def test_add_visit(self):
        request = self.c.get('/visit/%d/' % (self.test1.pk))
        self.test1 = TestModel.objects.get(pk=self.test1.pk)
        self.assertEqual(self.test1.visits, 1)

class VisitUrlTest(unittest.TestCase):
    pass
