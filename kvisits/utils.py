# -*- coding: utf-8 -*-
import hashlib
import datetime
from . import settings

def gen_hash(request, **kwargs):
    h = hashlib.sha1()
    for request_field in settings.KVISITS_REQUEST_FIELDS_FOR_HASH:
        h.update(request.META.get(request_field, ''))
    for arg in kwargs.values():
        h.update(str(arg))
    return h.hexdigest()
