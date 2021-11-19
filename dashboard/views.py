import json
import pandas as pd
import plotly
import plotly.express as px
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist

from .filters import MasterlistFilter


# Create your views here.
class Main_View(View):

    def get(self, request):

        # CDI Metrics Dictionary
        all_metrics_qs = CAPInstance.objects.values("date", "masterlist_count", "climate_collection_count")\
        .order_by("date")
        all_metrics = list(all_metrics_qs)

        # Current Status
        current_metrics_qs = all_metrics_qs.order_by("date").reverse()[:1] # Orders Newest Date First and selects top result
        current_metrics = list(current_metrics_qs)[0]
        
        # Total Warnings
        total_warnings_qs = CAPInstance.objects.values("cap_id", "date", "total_warnings").order_by("date").reverse()[:6]
        total_warnings = list(total_warnings_qs)
        
        graphJSON = self.generate_timeseries_chart(all_metrics)
        
        context = {'all_metrics':all_metrics, "current_metrics":current_metrics, "total_warnings":total_warnings, "graphJSON":graphJSON}

        return render(request, "HOMEPAGE.html", context)

    def generate_timeseries_chart(self, all_metrics):

        # Generatig Timeseries
        timeseries_df=pd.DataFrame({})
        for item in all_metrics:
            dct = {k:[v] for k,v in item.items()}
            timeseries_df=timeseries_df.append(pd.DataFrame.from_dict(dct))

        timeseries_df.columns=['Date', "Masterlist", "Climate Collection"]
        fig = px.line(timeseries_df, x='Date', y=timeseries_df.columns,
              hover_data={"Date": "|%B %d, %Y"},
              title='Timeseries')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON

class Charts_View(View):

    def get(self, request):

        return render(request, "metrics/METRICS.html")

class Warnings_View(View):

    def get(self, request):

        # All Warnings
        all_warnings_qs = CAPInstance.objects.values("cap_id", "date", "broken_urls", "lost_climate_tag","not_in_masterlist", "total_warnings")\
        .order_by("date").reverse()
        all_warnings = list(all_warnings_qs)

        context = {"all_warnings":all_warnings}

        return render(request, "warnings/WARNINGS.html", context)

class WarningsInstance_View(View):

    def get(self, request, **kwargs):

        cap_id = kwargs['cap_id']
        try:
            cap_instance = CAPInstance.objects.get(cap_id=cap_id)
        except:
            return HttpResponse("<html><h1>Page Not Found</h1></html>")

        # Grab Masterlist Atrributes
        brokenlist = self.dataset_fetcher(cap_instance, BrokenAPI)
        retaglist = self.dataset_fetcher(cap_instance, Retag)
        nimlist = self.get_nim(cap_instance)

        context = {'date': cap_instance.date, 'brokenlist':brokenlist[:5], 'retaglist': retaglist[:5], 'nimlist': nimlist[:5]}

        return render(request, "warnings/WARNINGS_INSTANCE.html", context)

    def dataset_fetcher(self, cap_id, model): 

        queryset = model.objects.filter(cap_id=cap_id)

        # Get Masterlist Attributes
        datasets = []

        for item in queryset:
            try:
                masterlist_obj = item.datagov_ID
            except:
                continue

            masterlist_dict = {
                                'title': masterlist_obj.title,
                                'catalog_url': masterlist_obj.catalog_url,
            }

            datasets.append(masterlist_dict)

        return datasets


    def get_nim(self, cap_instance):

        nim_qs = NotInMasterlist.objects.filter(cap_id=cap_instance).values('title', 'catalog_url')

        return list(nim_qs)
      
class Retag_View(View):

    def get(self, request):

        # Most Recent Cap Instance
        capinstance_qs = CAPInstance.objects.values().order_by("date").reverse()[:1]
        capinstance = list(capinstance_qs)[0] # Gets Dictionary of Most Recent Cap Instance
        date = capinstance['date']
        cap_id = capinstance['cap_id']


        # Get Retag Datasets from instance ID
        retag_qs = Retag.objects.filter(cap_id=cap_id)

        # Get Masterlist Attributes
        retag_datasets = []

        for retag in retag_qs:
            masterlist_obj = retag.datagov_ID

            masterlist_dict = {
                                'title': masterlist_obj.title,
                                'catalog_url': masterlist_obj.catalog_url,
                                'organization': masterlist_obj.organization,
                                'cdi_themes': masterlist_obj.cdi_themes,
                                'metadata_type' : masterlist_obj.metadata_type
            }

            retag_datasets.append(masterlist_dict)



        context = {'date':date, 'retaglist':retag_datasets}

        return render(request, "retag/RETAG.html", context)

class ClimateCollection_View(View):

    def get(self, request):

        return render(request, "climate_collection/CLIMATE_COLLECTION.html")

class Masterlist_View(View):

    def get(self, request):

        masterlist_qs = Masterlist.objects.values()

        ml_filter = MasterlistFilter(request.GET, queryset=masterlist_qs)
        masterlist = list(ml_filter.qs)

        return render(request, "cdi_masterlist/CDI_MASTERLIST.html", {'masterlist':masterlist, 'ml_filter':ml_filter})

class MasterlistDownload_View(View):

    def get(self, request):

        return render(request, "base.html")

class QAUpdates_View(View):

    def get(self, request):

        return render(request, "cdi_masterlist/qa_updates/QA_UPDATES.html")

