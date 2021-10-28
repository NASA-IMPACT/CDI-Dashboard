from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BaseView(TemplateView):
    template_name = "base.html"

def warnings(request):
    return render(request, "warnings/WARNINGS.html")

def warnings_instance(request):
    return render(request, "warnings/WARNINGS_INSTANCE.html")

def metrics(request):
    return render(request, "metrics/METRICS.html")

def retag(request):
    return render(request, "retag/RETAG.html")