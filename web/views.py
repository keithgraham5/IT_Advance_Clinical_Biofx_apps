from django.shortcuts import render
from .models import patient_identifier
from .models import variant_information

# Create your views here.
def variant_list(request):
    patients = patient_identifier.objects.all()
    variants = variant_information.objects.all()
    return render(request, 'web/variant_list.html', {'patients':patients, 'variants':variants})

