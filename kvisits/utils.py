# -*- coding: utf-8 -*-
import hashlib
import datetime
from . import settings

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now

def is_ignored(request, visit, url=True, bots=True, user_agents=True):
    if url:
        for ignored_url in settings.KVISITS_IGNORE_URLS:
            if request.META["PATH_INFO"].startswith(ignored_url):
                return True

    if user_agents and request.META.get("HTTP_USER_AGENT", "") in settings.KVISITS_IGNORE_USER_AGENTS:
        return True

    if bots and request.META.get("IS_BOT", False):
        return True

    if not visit.last_visit:
        return False

    time_since_last_visit = visit.last_visit + datetime.timedelta(minutes=settings.KVISITS_MIN_TIME_BETWEEN_VISITS)

    if time_since_last_visit < now():
        return False
    else:
        return True

def gen_hash(request, *args):
    h = hashlib.sha1()
    for request_field in settings.KVISITS_REQUEST_FIELDS_FOR_HASH:
        h.update(request.META.get(request_field, ''))
    for arg in args:
        h.update(str(arg))
    return h.hexdigest()
