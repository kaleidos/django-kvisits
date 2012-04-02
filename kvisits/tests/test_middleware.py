import unittest
from django.test.client import Client
from django.test.utils import override_settings
from .models import TestModel
from ..models import UrlVisit

class VisitUrlTest(unittest.TestCase):
    def setUp(self):
        self.c = Client()
        self.test1 = TestModel()
        self.test1.save()
        self.test2 = TestModel()
        self.test2.save()
        UrlVisit.objects.all().delete()

    def test_add_visit(self):
        request = self.c.get('/visit/%d/' % (self.test1.pk))
        self.assertEqual(UrlVisit.objects.all().count(), 1)
        request = self.c.get('/visit/%d/' % (self.test1.pk))
        self.assertEqual(UrlVisit.objects.all().count(), 1)
        request = self.c.get('/visit/%d/' % (self.test2.pk))
        self.assertEqual(UrlVisit.objects.all().count(), 2)
