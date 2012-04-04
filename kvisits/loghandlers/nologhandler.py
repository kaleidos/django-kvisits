from .loghandlerbase import LogHandlerBase

class NoLogHandler(LogHandlerBase):
    def log_object(self, obj, is_new, request, **kwargs):
        pass

    def log_url(self, url, is_new, request, **kwargs):
        pass
