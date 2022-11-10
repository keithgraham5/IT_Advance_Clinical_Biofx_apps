from django.shortcuts import render
from .models import patient_identifier

# Create your views here.
def variant_list(request):
    patients = patient_identifier.objects.all()
    return render(request, 'web/variant_list.html', {'patients':patients})

