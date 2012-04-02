from .ignorehandlerbase import IgnoreHandlerBase
import re
from kvisits.settings import KVISITS_IGNORE_URLS

class UrlIgnoreHandler(IgnoreHandlerBase):
    def check(self, request, **kwargs):
        url = kwargs.get('url', '')
        for regex in KVISITS_IGNORE_URLS:
            if re.match(regex, url):
                return True
        return False
