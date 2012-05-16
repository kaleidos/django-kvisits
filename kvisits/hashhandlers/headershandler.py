from .hashhandlerbase import HashHandlerBase
import hashlib
from .. import settings

class HeadersHandler(HashHandlerBase):
    def gen_hash(self, request, **kwargs):
        h = hashlib.sha1()
        for request_field in settings.KVISITS_REQUEST_FIELDS_FOR_HASH:
            h.update(request.META.get(request_field, ''))
        for arg in kwargs.values():
            h.update(str(arg))
        return h.hexdigest()

