from .ignorehandlerbase import IgnoreHandlerBase

class NoIgnoreHandler(IgnoreHandlerBase):
    def check(self, request, **kwargs):
        return False
