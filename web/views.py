from django.shortcuts import render

# Create your views here.
def variant_list(request):
    return render(request, 'web/variant_list.html', {})
