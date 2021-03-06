from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist

# Create your views here.
class Main_View(View):

    def get(self, request):

        # CDI Metrics Dictionary
        all_metrics_qs = CAPInstance.objects.values("date", "masterlist_count", "climate_collection_count")
        all_metrics = list(all_metrics_qs)

        # Current Status
        current_metrics_qs = all_metrics_qs.order_by("date").reverse()[:1] # Orders Newest Date First and selects top result
        current_metrics = list(current_metrics_qs)

        # Total Warnings
        total_warnings_qs = CAPInstance.objects.values("date", "total_warnings").order_by("date").reverse()
        total_warnings = list(total_warnings_qs)

        return render(request, "HOMEPAGE.html", {'all_metrics':all_metrics, "current_metrics":current_metrics, "total_warnings":total_warnings})

class Charts_View(View):

    def get(self, request):

        return render(request, "metrics/METRICS.html")

class Warnings_View(View):

    def get(self, request):

        # All Warnings
        all_warnings_qa = CAPInstance.objects.values("date", "broken_urls", "lost_climate_tag","not_in_masterlist", "total_warnings")\
        .order_by("date").reverse()
        all_warnings = list(all_warnings_qa)

        return render(request, "warnings/WARNINGS.html", {"all_warnings":all_warnings})

class WarningsInstance_View(View):

    def get(self, request):

        return render(request, "warnings/WARNINGS_INSTANCE.html")
      
class Retag_View(View):

    def get(self, request):

        return render(request, "retag/RETAG.html")

class ClimateCollection_View(View):

    def get(self, request):

        return render(request, "climate_collection/CLIMATE_COLLECTION.html")

class Masterlist_View(View):

    def get(self, request):

        return render(request, "cdi_masterlist/CDI_MASTERLIST.html")

class MasterlistDownload_View(View):

    def get(self, request):

        return render(request, "base.html")

class QAUpdates_View(View):

    def get(self, request):

        return render(request, "cdi_masterlist/qa_updates/QA_UPDATES.html")

