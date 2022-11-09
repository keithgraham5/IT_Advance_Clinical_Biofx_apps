from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone

class PID(models.Model):
    Name = models.CharField(max_length=100, null=False)
    Age = models.IntegerField(max=130, null=False)
    Relatives = models.BooleanField(null=True)


 def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title