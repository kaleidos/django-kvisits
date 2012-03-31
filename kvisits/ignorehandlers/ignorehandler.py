class IgnoreHandler(object):
    def check(self, request, *args):
        raise NotImplementedError
