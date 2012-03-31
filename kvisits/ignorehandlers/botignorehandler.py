from .ignorehandler import IgnoreHandler
from .. import settings

class BotIgnoreHandler(IgnoreHandler):
    def check(self, request, *args):
        return False
