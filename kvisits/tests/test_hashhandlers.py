import unittest
from django.http import HttpRequest
from django.test.utils import override_settings
from kvisits.hashhandlers.headershandler import HeadersHandler

class HeadersHandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = HeadersHandler()
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

    def test_gen_hash(self):
        expected_hash = 'ad48a3058b945d382f6d718ebe75631a13bc85d5'
        self.assertEqual(self.handler.gen_hash(self.request, data1=1, data2=2, data3=3), expected_hash)

