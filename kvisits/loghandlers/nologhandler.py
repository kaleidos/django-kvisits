from .loghandlerbase import LogHandlerBase

class NoLogHandler(LogHandlerBase):
    def log_object(self, amp, is_new, request, **kwargs):
        pass

    def log_url(self, url, is_new, request, **kwargs):
        pass
