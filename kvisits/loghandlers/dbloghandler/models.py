from django.contrib.auth.models import User
from django.db import models
from django.utils.importlib import import_module
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class LogObject(models.Model):
    request_meta = models.TextField()
    user = models.ForeignKey(User, related_name='visited_objects', null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    datetime = models.DateTimeField()

class LogUrl(models.Model):
    request_meta = models.TextField()
    user = models.ForeignKey(User, related_name='visited_urls', null=True, blank=True)
    url = models.URLField()
    datetime = models.DateTimeField()
