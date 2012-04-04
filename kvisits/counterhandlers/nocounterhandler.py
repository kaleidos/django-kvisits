from .counterhandlerbase import CounterHandlerBase

class NoCounterHandler(CounterHandlerBase):
    def add_obj_visit(self, request, obj, **kwargs):
        pass

    def add_url_visit(self, request, url, **kwargs):
        pass

    def get_obj_visits(self, request, obj, **kwargs):
        return 0

    def get_url_visits(self, request, url, **kwargs):
        return 0
