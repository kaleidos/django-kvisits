from .hashhandlerbase import Sha1HashHandler
from .. import settings

class HeadersHashHandler(Sha1HashHandler):
    def get_hash_items(self, request, **kwargs):
        items = []
        for request_field in settings.KVISITS_REQUEST_FIELDS_FOR_HASH:
            items.append(request.META.get(request_field, ''))
        for arg in kwargs.values():
            items.append(str(arg))
        return items

