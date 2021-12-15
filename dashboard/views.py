import ast
import io
import json
import openpyxl
import pandas as pd
import plotly
import plotly.express as px
import requests
import xlsxwriter
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str
from django.views.generic import TemplateView
from django.views import View
from openpyxl.writer.excel import save_virtual_workbook
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

        # Get Masterlist
        masterlist_qs = Masterlist.objects.values()
        masterlist = list(masterlist_qs)

        # Get Climate Tag Metrics
        recent_cap_qs = CAPInstance.objects.all().order_by("date").reverse()[:1]
        recent_cap = recent_cap_qs[0]

        climate_collection_count = recent_cap.climate_collection_count
        masterlist_count = recent_cap.masterlist_count
        notag_count = masterlist_count - climate_collection_count

        # Generate Charts
        agency_graph = self.generate_by_agency_chart(masterlist)
        theme_chart = self.generate_by_theme_chart(masterlist)
        geospatial_chart = self.generate_geospatial_chart(masterlist)
        climate_tag_chart = self.generate_climate_tag_chart(climate_collection_count, notag_count)

        context = {"agency_graphJSON": agency_graph, "theme_graphJSON": theme_chart,\
                     "geospatial_graphJSON": geospatial_chart, "climate_graphJSON": climate_tag_chart}

        return render(request, "metrics/METRICS.html", context)

    def generate_by_agency_chart(self, masterlist):
        pass

    def generate_by_theme_chart(self, masterlist):
        pass

    def generate_geospatial_chart(self, masterlist):
        pass

    def generate_climate_tag_chart(self, tag_count, notag_count):
        return [tag_count, notag_count]



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
            return render(request, "warnings/NOT_FOUND.html", {'user_input': cap_id})

        # Grab Masterlist Atrributes
        brokenlist = self.dataset_fetcher(cap_instance, BrokenAPI)
        retaglist = self.dataset_fetcher(cap_instance, Retag)
        nimlist = self.get_nim(cap_instance)

        context = {'date': cap_instance.date, 'brokenlist':brokenlist, 'retaglist': retaglist, 'nimlist': nimlist}

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
                                'metadata_type' : masterlist_obj.metadata_type,
                                'status': masterlist_obj.status
            }

            retag_datasets.append(masterlist_dict)



        context = {'date':date, 'retaglist':retag_datasets}

        return render(request, "retag/RETAG.html", context)

class Retag_Download(View):

    def get(self, request):

        # Get Retag Datasets
        date, retag_datasets_json = self.get_retag_request()
        retag_df = pd.DataFrame(retag_datasets_json)

        # Generate Excel File
        buffer = self.generate_xlsx(retag_df)

        buffer.seek(0)

        string_date = date.strftime("%m-%d-%Y")
        return FileResponse(buffer, as_attachment=True, filename='retag-request-{}.xlsx'.format(string_date))

    def get_retag_request(self):

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
                                'id': masterlist_obj.datagov_ID,
                                'name': masterlist_obj.name,
                                'catalog_url': masterlist_obj.catalog_url,
                                'cdi_themes': masterlist_obj.cdi_themes,
            }

            retag_datasets.append(masterlist_dict)

        return date, retag_datasets

    def generate_xlsx(self, dataframe):

        buffer = io.BytesIO() # Set First Stream

        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            dataframe.to_excel(writer, sheet_name='Retag Request', index=False)

        # Format Document
        workbook = openpyxl.load_workbook(buffer)

        worksheet = workbook.active

        # set the width of each column
        worksheet.column_dimensions['A'].width = 35
        worksheet.column_dimensions['B'].width = 65
        worksheet.column_dimensions['C'].width = 55
        worksheet.column_dimensions['D'].width = 55

        for row in worksheet.iter_rows():
            for cell in row:      
                cell.alignment = openpyxl.styles.Alignment(wrapText=True)
      
        # save the file
        buffer = io.BytesIO(save_virtual_workbook(workbook)) # Update Stream w/ Formatting

        return buffer

class ClimateCollection_View(View):

    def get(self, request):

        try:
            climate_collection_json = self.fetch_climate_collection()
        except:
            return render(request, "climate_collection/NOT_FOUND.html")
            

        context = {'climate_collection': climate_collection_json}

        return render(request, "climate_collection/CLIMATE_COLLECTION.html", context)

    def fetch_climate_collection(self):

        api_call = requests.get('https://catalog.data.gov/api/3/action/package_search?fq=groups:climate5434&rows=2000').json()
        cdi_datasets = api_call['result']['results']

        # Create Desired Dictionary

        datasets_json = []

        for dataset in cdi_datasets:
            dataset_dict = {}

            dataset_dict['title'] = dataset['title']
            dataset_dict['catalog_url'] = 'https://catalog.data.gov/dataset/{}'.format(dataset['name'])
            dataset_dict['api_url'] = 'https://catalog.data.gov/api/3/action/package_show?id={}'.format(dataset['id'])
            dataset_dict['organization'] = dataset['organization']['name']


            datasets_json.append(dataset_dict)

        return datasets_json


class Masterlist_View(View):

    def get(self, request):

        masterlist_qs = Masterlist.objects.values()

        ml_filter = MasterlistFilter(request.GET, queryset=masterlist_qs)
        masterlist = list(ml_filter.qs)
        
        context = {'masterlist':masterlist, 'ml_filter':ml_filter}

        return render(request, "cdi_masterlist/CDI_MASTERLIST.html", context)

class MasterlistDownload_View(View):

    def get(self, request):

        masterlist_qs = Masterlist.objects.values()
        masterlist = list(masterlist_qs)

        masterlist_json = json.dumps(masterlist, indent=4)

        # Get Date
        capinstance_qs = CAPInstance.objects.values().order_by("date").reverse()[:1]
        capinstance = list(capinstance_qs)[0] # Gets Dictionary of Most Recent Cap Instance
        date = capinstance['date']

        string_date = date.strftime("%m-%d-%Y")
        filename = "CDI_Masterlist_{}.json".format(string_date)

        response = HttpResponse(masterlist_json, content_type = "application/force-download")
        response['Content-Disposition'] = 'attachment; filename={}'.format(smart_str(filename))
        return response
        

class QAUpdates_View(View):

    def get(self, request):

        caps = CAPInstance.objects.all().order_by("date").reverse()

        qaupdates = []

        for capinstance in caps:

            date = capinstance.date

            qa_qs = QAUpdates.objects.filter(cap_id=capinstance).values()
            qalist = list(qa_qs)
            
            for qa in qalist:
                try:
                    qa['name'] = self.json_converter(qa['name'])
                except:
                    pass
                try:
                    qa['title'] = self.json_converter(qa['title'])
                except:
                    pass
                try:
                    qa['catalog_url'] = self.json_converter(qa['catalog_url'])
                except:
                    pass
                try:
                    qa['organization'] = self.json_converter(qa['organization'])
                except:
                    pass
                try:
                    qa['metadata_type'] = self.json_converter(qa['metadata_type'])
                except:
                    pass

            if len(qalist) == 0:
                continue

            instance_qa = {"date": date, "qalist": qalist}

            qaupdates.append(instance_qa)

        context = {'qaupdates': qaupdates}

        return render(request, "cdi_masterlist/qa_updates/QA_UPDATES.html", context)

    def json_converter(self, json_string):

        cdi_dict = ast.literal_eval(json_string)
        formatted_string = "Invalid: {}\nUpdated: {}".format(cdi_dict['Invalid'], cdi_dict['Updated'])

        return formatted_string







