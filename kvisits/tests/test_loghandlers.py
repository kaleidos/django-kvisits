import unittest
from django.http import HttpRequest
from django.contrib.auth.models import User, AnonymousUser
from kvisits.loghandlers.nologhandler import NoLogHandler
from kvisits.loghandlers.dbloghandler import DBLogHandler
from kvisits.loghandlers.dbloghandler.models import *
from .models import TestModel

class NoLogHandlerTest(unittest.TestCase):
    def setUp(self):
        self.test1 = TestModel()
        self.test1.save()
        self.logger = NoLogHandler()

    def test_log_object(self):
        self.logger.log_object(self.test1._amp(), True, HttpRequest(), data1=1, data2=2, data3=3)

    def test_log_url(self):
        self.logger.log_url('/visit/%d/' % (self.test1.pk), True, HttpRequest(), data1=1, data2=2, data3=3)


class DBLogHandlerTest(unittest.TestCase):
    def setUp(self):
        self.test1 = TestModel()
        self.test1.save()
        self.logger = DBLogHandler()

        (self.user, is_new) = User.objects.get_or_create(username="test-user")
        self.user.save()
        self.user_request = HttpRequest()
        self.user_request.user = self.user
        self.user_request.META = {'header1': 'test1', 'header2': 'test2'}

        self.anon = AnonymousUser()
        self.anon_request = HttpRequest()
        self.anon_request.user = self.anon
        self.anon_request.META = {'header1': 'test1', 'header2': 'test2'}

    def test_log_object(self):
        self.assertEqual(LogObject.objects.count(), 0)
        self.assertEqual(LogUrl.objects.count(), 0)

        self.logger.log_object(self.test1._amp(), True, self.user_request, data1=1, data2=2, data3=3)
        self.assertEqual(LogObject.objects.count(), 1)

        self.logger.log_object(self.test1._amp(), True, self.anon_request, data1=1, data2=2, data3=3)
        self.assertEqual(LogObject.objects.count(), 2)

        self.assertEqual(LogObject.objects.count(), 2)
        self.assertEqual(LogUrl.objects.count(), 0)

    def test_log_url(self):
        self.assertEqual(LogObject.objects.count(), 0)
        self.assertEqual(LogUrl.objects.count(), 0)

        self.logger.log_url('/visit/%d/' % (self.test1.pk), True, self.user_request, data1=1, data2=2, data3=3)
        self.assertEqual(LogUrl.objects.count(), 1)

        self.logger.log_url('/visit/%d/' % (self.test1.pk), True, self.anon_request, data1=1, data2=2, data3=3)
        self.assertEqual(LogUrl.objects.count(), 2)

        self.assertEqual(LogObject.objects.count(), 0)
        self.assertEqual(LogUrl.objects.count(), 2)

    def tearDown(self):
        LogObject.objects.all().delete()
        LogUrl.objects.all().delete()
