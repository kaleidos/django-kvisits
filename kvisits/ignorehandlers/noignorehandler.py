from .ignorehandler import IgnoreHandler

class NoIgnoreHandler(IgnoreHandler):
    def check(self, request, *args):
        return False
