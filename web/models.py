from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone

class variant_information(models.Model):
    g_nomenclature = models.CharField(max_length=100, null=False)
    variant_protein = models.CharField(max_length=100, null=False) #Variant Protein
    c_nomenclature = models.CharField(max_length=100, null=False) #Variant cDNA

class patient_identifier(models.Model):
    forename = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=130, null=False)
    age = models.CharField(max_length=130, null=False)
    proband = models.CharField(max_length=100, null=False)
    affected_relatives = models.CharField(max_length=100, null=False)
    tumor = models.CharField(max_length=100, null=False) #Description
    Stage = models.CharField(max_length=100, null=False, default="blank") #Tumor stage
    sequencer = models.CharField(max_length=100, null=False)
    g_nomenclature = models.ForeignKey(variant_information, db_column='g_nomenclature', on_delete=models.CASCADE)
    pathogenecity_code = models.CharField(max_length=100, null=False)
    evidence_codes = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.g_nomenclature
#Stage

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
