from django.shortcuts import render
from .models import patient_identifier
from django.contrib.auth.models import User
from .filter import PatientFilter

# Create your views here.
def variant_list(request):
    patients = patient_identifier.objects.all()
    return render(request, 'web/variant_list.html', {'patients':patients})

def search(request):
    patients = patient_identifier.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=patients)
    return render(request, 'web/filter_list.html', {'filter': patient_filter})
