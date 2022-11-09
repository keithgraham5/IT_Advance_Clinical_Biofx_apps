from django.contrib import admin
from .models import patient_identifier
from .models import variant_information

admin.site.register(patient_identifier)
admin.site.register(variant_information)
# Register your models here.
