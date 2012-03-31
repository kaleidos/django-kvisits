class LogHandler(object):
    def log_object(self, amp, is_new, request, *args):
        raise NotImplementedError
    def log_url(self, url, is_new, request, *args):
        raise NotImplementedError
