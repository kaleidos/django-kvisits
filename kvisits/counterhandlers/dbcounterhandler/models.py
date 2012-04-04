from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class UrlVisit(models.Model):
    url = models.CharField(max_length=200, unique=True)
    visits = models.IntegerField(null=False, blank=False, default=0)


class ObjVisit(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    visits = models.IntegerField(null=False, blank=False, default=0)


class KVisitableMixin(models.Model):
    visits = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        abstract = True
