from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BaseView(TemplateView):
    template_name = "HOMEPAGE.html"

def warnings(request):
    return render(request, "warnings/WARNINGS.html")

def warnings_instance(request):
    return render(request, "warnings/WARNINGS_INSTANCE.html")

def metrics(request):
    return render(request, "metrics/METRICS.html")

def retag(request):
    return render(request, "retag/RETAG.html")

def cdi_masterlist(request):
    return render(request, "cdi_masterlist/CDI_MASTERLIST.html")

def qa_updates(request):
    return render(request, "cdi_masterlist/qa_updates/QA_UPDATES.html")

def climate_collection(request):
    return render(request, "CLIMATE_COLLECTION.html")