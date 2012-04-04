class CounterHandlerBase(object):
    def add_url_visit(self, request, url, **kwargs):
        raise NotImplementedError

    def add_obj_visit(self, request, obj, **kwargs):
        raise NotImplementedError

    def get_url_visits(self, request, url, **kwargs):
        raise NotImplementedError

    def get_obj_visits(self, request, obj, **kwargs):
        raise NotImplementedError
