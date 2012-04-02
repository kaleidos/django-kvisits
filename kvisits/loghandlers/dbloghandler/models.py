from django.contrib.auth.models import User
from django.db import models

class LogObject(models.Model):
    request_meta = models.TextField()
    user = models.ForeignKey(User, related_name='visited_objects', null=True, blank=True)
    app_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    obj_pk = models.CharField(max_length=50)
    datetime = models.DateTimeField()

class LogUrl(models.Model):
    request_meta = models.TextField()
    user = models.ForeignKey(User, related_name='visited_urls', null=True, blank=True)
    url = models.URLField()
    datetime = models.DateTimeField()
