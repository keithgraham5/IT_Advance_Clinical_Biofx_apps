from django.shortcuts import render
from .models import patient_identifier
from .models import variant_information

# Create your views here.
def variant_list(request):
    patients = patient_identifier.objects.all()
    variants = variant_information.objects.all()
    return render(request, 'web/variant_list.html', {'patients':patients, 'variants':variants})

def searchpage(request):
    srh = request.GET['query']
    patients = \
    patient_identifier.objects.filter(forename__icontains=srh) | \
    patient_identifier.objects.filter(surname__icontains=srh) | \
    patient_identifier.objects.filter(age__icontains=srh) | \
    patient_identifier.objects.filter(proband__icontains=srh) | \
    patient_identifier.objects.filter(affected_relatives__icontains=srh) | \
    patient_identifier.objects.filter(tumor__icontains=srh) | \
    patient_identifier.objects.filter(Stage__icontains=srh) | \
    patient_identifier.objects.filter(sequencer__icontains=srh) | \
    patient_identifier.objects.filter(forename__icontains=srh) | \
    patient_identifier.objects.filter(pathogenecity_code__icontains=srh) | \
    patient_identifier.objects.filter(evidence_codes__icontains=srh) | \
    patient_identifier.objects.filter(g_nomenclature__g_nomenclature__icontains=srh) | \
    patient_identifier.objects.filter(g_nomenclature__c_nomenclature__icontains=srh) | \
    patient_identifier.objects.filter(g_nomenclature__variant_protein__icontains=srh)
    params = {'patients':patients,'search': srh}
    return render(request, 'web/search_page.html', params)
