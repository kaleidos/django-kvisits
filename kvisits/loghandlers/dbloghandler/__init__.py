from ..loghandlerbase import LogHandlerBase
from .models import LogObject, LogUrl
import datetime
import simplejson

class DBLogHandler(LogHandlerBase):
    def log_object(self, obj, is_new, request, **kwargs):
        log = LogObject()
        log.request_meta = simplejson.dumps(request.META)
        if request.user.is_anonymous():
            log.user = None
        else:
            log.user = request.user
        log.content_object = obj
        log.datetime = datetime.datetime.now()
        log.save()

    def log_url(self, url, is_new, request, **kwargs):
        log = LogUrl()
        log.request_meta = simplejson.dumps(request.META)
        if request.user.is_anonymous():
            log.user = None
        else:
            log.user = request.user
        log.url = url
        log.datetime = datetime.datetime.now()
        log.save()
