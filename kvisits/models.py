from django.db import models
from django.contrib.auth.models import User
from .utils import *
from .uniqhandlers import uniqhandler
from .ignorehandlers import ignorehandler
from .loghandlers import loghandler

class KVisitableMixin(models.Model):
    visits = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        abstract = True

    # Object representation in format (App, Model, PK)
    def _amp(self):
        return (
            unicode(self.Meta.app_name),
            unicode(self.__class__.__name__),
            unicode(self.pk)
        )

    def add_visit(self, request, *args):
        hash=gen_hash(request, *args)
        is_new = uniqhandler.check(hash)
        is_ignored = ignorehandler.check(request, *args)

        if is_new and not is_ignored:
            self.visits += 1
            self.save()

        if settings.KVISITS_LOG_ENABLED:
            loghandler.log_object(self._amp(), is_new, request, *args)

    def get_history_users_qs(self):
        qs = KVisitObjectHistoryUser.all()
        amp = self._amp()
        return qs.filter(app_name=amp[0], model_name=amp[1], pk=amp[0])

    def get_history_requests_qs(self):
        qs = KVisitObjectHistoryRequest.all()
        amp = self._amp()
        return qs.filter(app_name=amp[0], model_name=amp[1], pk=amp[0])
