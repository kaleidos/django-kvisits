class IgnoreHandlerBase(object):
    def check(self, request, *args):
        raise NotImplementedError
