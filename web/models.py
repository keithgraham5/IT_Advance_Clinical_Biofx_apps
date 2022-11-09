from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
  

  
# creating a form 
class GeeksForm(forms.Form):
    geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)

class PID(models.Model):
    Name = models.CharField(max_length=100, null=False)
    Age = models.IntegerField(max=130, null=False)
    Relatives = models.BooleanField(null=True)


class Tumor_Type(model.Models):
    Tumor_Type = models.CharField(max_length=100)

# iterable
SequencerChoices = [
    'MiSeq',
    'HiSeq',
    'NextSeq',
    ]

class TableSequencer(models.Model):
    Sequencer = models.CharField(choices=SequencerChoices)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
