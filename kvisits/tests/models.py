from kvisits.counterhandlers.dbcounterhandler.models import KVisitableMixin
from django.db import models

class TestModel(KVisitableMixin):
    pass

class TestModel2(models.Model):
    pass
