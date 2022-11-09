from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
  

  
# creating a form 
class GeeksForm(forms.Form):
    geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)

class patient_identifier(models.Model):
    forename = models.CharField(max_length=100, null=False)
    surname = models.IntegerField(max=130, null=False)
    age = models.BooleanField(null=True)
    proband = models.CharField(max_length=100, null=False)
    affected_relatives = models.CharField(max_length=100, null=False)
    tumor = models.CharField(max_length=100, null=False)
    sequencer = models.CharField(max_length=100, null=False)
    g_nomenclature = models.CharField(max_length=100, null=False)
    pathogenecity_code = models.CharField(max_length=100, null=False)
    evidence_codes = models.CharField(max_length=100)

class variant_information(models.Model):
    g_nomenclature = models.ForeignKey(patient_identifier, db_column='g_nomenclature', on_delete=models.CASCADE)
    variant_protein = models.CharField(max_length=100, null=False)
    c_nomenclature = models.CharField(max_length=100, null=False)
    
class evidence_codes(models.Model):
    code_ID = models.ForeignKey(patient_identifier, db_column='evidence_codes', on_delete=models.CASCADE)
    evidence_codes = models.CharField(max_length=100, null=False)

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
