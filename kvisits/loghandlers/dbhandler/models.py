from django.contrib.auth.models import User

class LogUrlRequest(models.Model):
    request_data = models.TextField()
    url = models.URLField()
    datetime = models.DatetimeField()

class LogObjectRequest(models.Model):
    request_data = models.TextField()
    app_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    pk = models.CharField(max_length=50)
    datetime = models.DatetimeField()

class LogUrlUser(models.Model):
    user = models.ForeignKey(User, related_name='visited_urls')
    url = models.URLField()
    datetime = models.DatetimeField()

class LogObjectUser(models.Model):
    user = models.ForeingKey(User, related_name='visited_objects')
    app_name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    pk = models.CharField(max_length=50)
    datetime = models.DatetimeField()
