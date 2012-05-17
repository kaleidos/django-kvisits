import unittest
from django.http import HttpRequest
from django.test.utils import override_settings
from kvisits.counterhandlers.nocounterhandler import NoCounterHandler
from kvisits.counterhandlers.dbcounterhandler import DBCounterHandler
from kvisits.counterhandlers.dbcounterhandler.models import *
from .models import TestModel, TestModel2

class NoCounterHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = NoCounterHandler()
        self.request = HttpRequest()
        self.request.META = {
            'CONTENT_LENGTH': '',
            'CONTENT_TYPE': 'text/html',
            'HTTP_ACCEPT_ENCODING': 'utf-8',
            'HTTP_ACCEPT_LANGUAGE': 'es',
            'HTTP_HOST': 'testhost',
            'HTTP_REFERER': 'testreferer',
            'HTTP_USER_AGENT': 'test user agent',
            'QUERY_STRING': '/',
            'REMOTE_ADDR': 'testaddress',
            'REMOTE_HOST': 'testhost',
            'REMOTE_USER': 'testuser',
            'REQUEST_METHOD': 'GET',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': '80',
        }
        self.test1 = TestModel()
        self.test1.save()

    def test_add_url_visit(self):
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 0)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit/%d/" % self.test1.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 0)

    def test_add_obj_visit(self):
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 0)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test1, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 0)

    def test_get_url_visits(self):
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 0)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit/%d/" % self.test1.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 0)

    def test_get_obj_visits(self):
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 0)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test1, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 0)

class DBCounterHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = DBCounterHandler()
        self.request = HttpRequest()
        self.request.META = {
            'CONTENT_LENGTH': '',
            'CONTENT_TYPE': 'text/html',
            'HTTP_ACCEPT_ENCODING': 'utf-8',
            'HTTP_ACCEPT_LANGUAGE': 'es',
            'HTTP_HOST': 'testhost',
            'HTTP_REFERER': 'testreferer',
            'HTTP_USER_AGENT': 'no-ignore',
            'QUERY_STRING': '/',
            'REMOTE_ADDR': 'testaddress',
            'REMOTE_HOST': 'testhost',
            'REMOTE_USER': 'testuser',
            'REQUEST_METHOD': 'GET',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': '80',
        }
        UrlVisit.objects.all().delete()
        ObjVisit.objects.all().delete()

        self.test1 = TestModel()
        self.test1.visits = 0
        self.test1.save()
        self.test2 = TestModel2()
        self.test2.save()

    def test_add_url_visit(self):
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 0)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit/%d/" % self.test1.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 1)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit/%d/" % self.test1.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 2)

        self.assertEqual(self.handler.get_url_visits(self.request, "/visit2/%d/" % self.test2.pk), 0)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit2/%d/" % self.test2.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit2/%d/" % self.test2.pk), 1)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit2/%d/" % self.test2.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit2/%d/" % self.test2.pk), 2)

    def test_add_obj_visit(self):
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 0)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test1, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 1)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test1, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 2)

        self.assertEqual(self.handler.get_obj_visits(self.request, self.test2), 0)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test2, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test2), 1)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test2, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test2), 2)

    def test_get_url_visits(self):
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 0)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit/%d/" % self.test1.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 1)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit/%d/" % self.test1.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit/%d/" % self.test1.pk), 2)

        self.assertEqual(self.handler.get_url_visits(self.request, "/visit2/%d/" % self.test2.pk), 0)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit2/%d/" % self.test2.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit2/%d/" % self.test2.pk), 1)
        self.assertEqual(self.handler.add_url_visit(self.request, "/visit2/%d/" % self.test2.pk, 'xxx'), None)
        self.assertEqual(self.handler.get_url_visits(self.request, "/visit2/%d/" % self.test2.pk), 2)

    def test_get_obj_visits(self):
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 0)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test1, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 1)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test1, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test1), 2)

        self.assertEqual(self.handler.get_obj_visits(self.request, self.test2), 0)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test2, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test2), 1)
        self.assertEqual(self.handler.add_obj_visit(self.request, self.test2, 'xxx'), None)
        self.assertEqual(self.handler.get_obj_visits(self.request, self.test2), 2)
