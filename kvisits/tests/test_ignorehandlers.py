import unittest
from django.http import HttpRequest
from django.test.utils import override_settings
from kvisits.ignorehandlers.noignorehandler import NoIgnoreHandler
from kvisits.ignorehandlers.useragentignorehandler import UserAgentIgnoreHandler

class NoIgnoreHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = NoIgnoreHandler()
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

    def test_check(self):
        self.assertEqual(self.handler.check(self.request, 1, 2, 3), False)

class UserAgentIgnoreHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = UserAgentIgnoreHandler()
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
    def test_check(self):
        self.assertEqual(self.handler.check(self.request, 1, 2, 3), True)
