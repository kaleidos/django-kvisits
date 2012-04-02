from .ignorehandlerbase import IgnoreHandlerBase

class NoIgnoreHandler(IgnoreHandlerBase):
    def check(self, request, *args):
        return False
