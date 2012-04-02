import unittest
from django.http import HttpRequest
from django.test.utils import override_settings
from kvisits.uniqhandlers.nouniqhandler import NoUniqHandler
from kvisits.uniqhandlers.dbuniqhandler import DBUniqHandler
from kvisits.uniqhandlers.dbuniqhandler.models import DBUniqHandlerHashes
import hashlib
import time

class NoUniqHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = NoUniqHandler()
        self.hash = hashlib.sha1("test1").hexdigest()

    def test_check(self):
        self.assertEqual(self.handler.check(self.hash), True)
        self.assertEqual(self.handler.check(self.hash), True)

    def test_cleanup(self):
        self.handler.cleanup()

class DBUniqHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = DBUniqHandler()
        self.hash1 = hashlib.sha1("test1").hexdigest()
        self.hash2 = hashlib.sha1("test2").hexdigest()
        self.hash3 = hashlib.sha1("test3").hexdigest()

    def test_check(self):
        self.assertEqual(self.handler.check(self.hash1), True)
        self.assertEqual(self.handler.check(self.hash1), False)
        time.sleep(2)
        self.assertEqual(self.handler.check(self.hash1), True)

    def test_cleanup(self):
        self.assertEqual(self.handler.check(self.hash1), True)
        self.assertEqual(self.handler.check(self.hash2), True)
        self.assertEqual(self.handler.check(self.hash3), True)
        self.assertEqual(DBUniqHandlerHashes.objects.all().count(), 3)
        self.handler.cleanup()
        self.assertEqual(DBUniqHandlerHashes.objects.all().count(), 3)
        time.sleep(2)
        self.assertEqual(self.handler.check(self.hash1), True)
        self.assertEqual(DBUniqHandlerHashes.objects.all().count(), 3)
        self.handler.cleanup()
        self.assertEqual(DBUniqHandlerHashes.objects.all().count(), 1)

    def tearDown(self):
        DBUniqHandlerHashes.objects.all().delete()
