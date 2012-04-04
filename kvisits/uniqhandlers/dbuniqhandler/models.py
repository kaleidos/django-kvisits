from django.db import models

class DBUniqHandlerHashes(models.Model):
    visit_hash = models.CharField(max_length=255, primary_key=True)
    last_counted_visit = models.DateTimeField()
