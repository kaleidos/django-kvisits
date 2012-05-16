from . import settings
from .hashhandlers import hashhandler
from .uniqhandlers import uniqhandler
from .ignorehandlers import ignorehandlers
from .loghandlers import loghandlers
from .counterhandlers import counterhandler
from django.contrib.contenttypes.models import ContentType


def add_url_visit(request, url, **kwargs):
    visit_hash=hashhandler.gen_hash(request, url=url, **kwargs)
    is_new = uniqhandler.check(visit_hash)
    is_ignored = False
    
    for ignorehandler in ignorehandlers:
        if ignorehandler.check(request, url=url, **kwargs):
            is_ignored = True
            break
    
    if is_new and not is_ignored:
        counterhandler.add_url_visit(request, url, **kwargs)
    
    if settings.KVISITS_LOG_ENABLED:
        for loghandler in loghandlers:
            loghandler.log_url(url, is_new, request, url=url, **kwargs)

def add_obj_visit(request, obj, **kwargs):
    obj_content_type = ContentType.objects.get_for_model(obj)
    visit_hash=hashhandler.gen_hash(
            request,
            app_label=obj_content_type.app_label,
            model=obj_content_type.model,
            pk=obj.pk,
            **kwargs
    )
    is_new = uniqhandler.check(visit_hash)
    is_ignored = False

    for ignorehandler in ignorehandlers:
        if ignorehandler.check(request, **kwargs):
            is_ignored = True
            break

    if is_new and not is_ignored:
        counterhandler.add_obj_visit(request, obj, **kwargs)

    if settings.KVISITS_LOG_ENABLED:
        for loghandler in loghandlers:
            loghandler.log_object(obj, is_new, request, **kwargs)
