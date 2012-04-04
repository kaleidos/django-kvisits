class LogHandlerBase(object):
    def log_object(self, obj, is_new, request, **kwargs):
        raise NotImplementedError
    def log_url(self, url, is_new, request, **kwargs):
        raise NotImplementedError
