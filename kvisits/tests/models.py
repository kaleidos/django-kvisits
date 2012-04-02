from ..models import KVisitableMixin
from django.db import models

class TestModel(KVisitableMixin, models.Model):
    pass
