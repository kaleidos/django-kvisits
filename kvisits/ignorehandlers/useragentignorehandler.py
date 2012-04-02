from .ignorehandlerbase import IgnoreHandlerBase
import re
from kvisits.settings import KVISITS_IGNORE_USER_AGENTS

class UserAgentIgnoreHandler(IgnoreHandlerBase):
    def check(self, request, *args):
        for regex in KVISITS_IGNORE_USER_AGENTS:
            if re.match(regex, request.META['HTTP_USER_AGENT']):
                return True
        return False
