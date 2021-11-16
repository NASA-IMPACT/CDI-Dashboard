from django.urls import include, path
from .views import *

urlpatterns = [
    path("", Main_View.as_view(), name="main"),
    path("charts", Charts_View.as_view(), name="charts"),
    path("retag", Retag_View.as_view(), name="retag"),
    path("warnings", Warnings_View.as_view(), name="warnings"),
    path("warnings/<str:cap_id>", WarningsInstance_View.as_view(), name="warningsinstance"),
    path("climate-collection", ClimateCollection_View.as_view(), name="climatecollection"),
    path("cdi-masterlist", Masterlist_View.as_view(), name="masterlist"),
    path("cdi-masterlist/download", MasterlistDownload_View.as_view(), name="masterlistdownload"),
    path("cdi-masterlist/qa-updates", QAUpdates_View.as_view(), name="qaupdates"),

]