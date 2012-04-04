import unittest
from django.test.client import Client
from django.test.utils import override_settings
from django.http import HttpRequest
from .models import TestModel
from kvisits.counterhandlers.dbcounterhandler.models import UrlVisit
from kvisits.counterhandlers import counterhandler

class VisitUrlTest(unittest.TestCase):
    def setUp(self):
        self.c = Client()
        self.test1 = TestModel()
        self.test1.save()
        self.test2 = TestModel()
        self.test2.save()
        UrlVisit.objects.all().delete()

    def test_add_visit(self):
        self.assertEqual(counterhandler.get_url_visits(HttpRequest(), '/visit/%d/' % (self.test1.pk)), 0)
        request = self.c.get('/visit/%d/' % (self.test1.pk))
        self.assertEqual(counterhandler.get_url_visits(HttpRequest(), '/visit/%d/' % (self.test1.pk)), 1)
        request = self.c.get('/visit/%d/' % (self.test1.pk))
        self.assertEqual(counterhandler.get_url_visits(HttpRequest(), '/visit/%d/' % (self.test1.pk)), 1)
        self.assertEqual(counterhandler.get_url_visits(HttpRequest(), '/visit/%d/' % (self.test2.pk)), 0)
        request = self.c.get('/visit/%d/' % (self.test2.pk))
        self.assertEqual(counterhandler.get_url_visits(HttpRequest(), '/visit/%d/' % (self.test2.pk)), 1)
