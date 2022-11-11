from .models import patient_identifier
import django_filters

class PatientFilter(django_filters.FilterSet):
    forename = django_filters.CharFilter(lookup_expr='icontains')
    surname = django_filters.CharFilter(lookup_expr='icontains')
    g_nomenclature = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = patient_identifier
        fields = ['forename', 'surname', 'age', 'proband', 'affected_relatives', 'tumor', 'Stage', 'sequencer', 'g_nomenclature', 'pathogenecity_code', 'evidence_codes',]
