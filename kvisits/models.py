from django.db import models
from django.contrib.auth.models import User
from .utils import *
from .uniqhandlers import uniqhandler
from .ignorehandlers import ignorehandlers
from .loghandlers import loghandlers

class UrlVisitManager(models.Manager):
    def add_visit(self, request, url, **kwargs):
        hash=gen_hash(request, url=url, **kwargs)
        is_new = uniqhandler.check(hash)
        is_ignored = False

        for ignorehandler in ignorehandlers:
            if ignorehandler.check(request, url=url, **kwargs):
                is_ignored = True
                break

        if is_new and not is_ignored:
            (urlvisit, created) = self.get_or_create(url=url)
            urlvisit.visits += 1
            urlvisit.save()

        if settings.KVISITS_LOG_ENABLED:
            for loghandler in loghandlers:
                loghandler.log_object(self, is_new, request, url=url, **kwargs)

class UrlVisit(models.Model):
    url = models.CharField(max_length=200, unique=True)
    visits = models.IntegerField(null=False, blank=False, default=0)

    objects = UrlVisitManager()

class KVisitableMixin(models.Model):
    visits = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        abstract = True

    # Object representation in format (App, Model, PK)
    def add_visit(self, request, **kwargs):
        hash=gen_hash(request, **kwargs)
        is_new = uniqhandler.check(hash)
        is_ignored = False

        for ignorehandler in ignorehandlers:
            if ignorehandler.check(request, **kwargs):
                is_ignored = True
                break

        if is_new and not is_ignored:
            self.visits += 1
            self.save()

        if settings.KVISITS_LOG_ENABLED:
            for loghandler in loghandlers:
                loghandler.log_object(self, is_new, request, **kwargs)
