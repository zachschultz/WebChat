import datetime
from django.utils import timezone
from django.db import models

class Message(models.Model):
  # owner = models.ForeignKey('auth.User', related_name='messages')
  creator = models.CharField(max_length=15, default="Anonymous")
  content = models.CharField(max_length=200)
  post_date = models.DateTimeField('date posted', default=timezone.now())
  def was_posted_recently(self):
    return self.post_date >= timezone.now() - datetime.timedelta(days=1)
  def __str__(self):
    return (self.creator + self.content)

# Create your models here.
