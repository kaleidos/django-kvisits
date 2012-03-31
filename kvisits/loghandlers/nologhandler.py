class NoLogHandler(object):
    def log_object(self, amp, is_new, request, *args):
        pass

    def log_url(self, url, is_new, request, *args):
        pass
