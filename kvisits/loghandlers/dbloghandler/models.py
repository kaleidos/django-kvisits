from django.contrib.auth.models import User
from django.db import models
from django.utils.importlib import import_module

class LogObject(models.Model):
    request_meta = models.TextField()
    user = models.ForeignKey(User, related_name='visited_objects', null=True, blank=True)
    app_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    obj_pk = models.CharField(max_length=50)
    datetime = models.DateTimeField()

    def get_amp_object(self):
        amp_class = getattr(import_module(self.app_name+".models"), self.model_name)
        try:
            return amp_class.objects.get(pk=self.obj_pk)
        except amp_class.DoesNotExist:
            return None

class LogUrl(models.Model):
    request_meta = models.TextField()
    user = models.ForeignKey(User, related_name='visited_urls', null=True, blank=True)
    url = models.URLField()
    datetime = models.DateTimeField()
