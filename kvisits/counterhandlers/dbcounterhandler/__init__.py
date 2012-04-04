from ..counterhandlerbase import CounterHandlerBase
from .models import *

class DBCounterHandler(CounterHandlerBase):
    def add_url_visit(self, request, url, **kwargs):
        (url_visit_counter, created) = UrlVisit.objects.get_or_create(url=url)
        url_visit_counter.visits += 1
        url_visit_counter.save()

    def add_obj_visit(self, request, obj, **kwargs):
        if isinstance(obj, KVisitableMixin):
            obj.visits += 1
            obj.save()
        else:
            obj_content_type = ContentType.objects.get_for_model(obj)
            (obj_visit_counter, created) = ObjVisit.objects.get_or_create(content_type=obj_content_type, object_id=obj.pk)
            obj_visit_counter.visits += 1
            obj_visit_counter.save()

    def get_url_visits(self, request, url, **kwargs):
        try:
            url_visit_counter = UrlVisit.objects.get(url=url)
            return url_visit_counter.visits
        except UrlVisit.DoesNotExist:
            return 0

    def get_obj_visits(self, request, obj, **kwargs):
        if isinstance(obj, KVisitableMixin):
            return obj.visits
        else:
            try:
                obj_content_type = ContentType.objects.get_for_model(obj)
                obj_visit_counter = ObjVisit.objects.get(content_type=obj_content_type, object_id=obj.pk)
                return obj_visit_counter.visits
            except ObjVisit.DoesNotExist:
                return 0
