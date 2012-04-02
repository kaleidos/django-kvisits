class IgnoreHandlerBase(object):
    def check(self, request, **kwargs):
        raise NotImplementedError
