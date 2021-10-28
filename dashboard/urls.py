from django.urls import include, path

from .views import BaseView
from . import views

urlpatterns = [
    path("", BaseView.as_view(), name="dashboard_base"),
    path("warnings", views.warnings, name = "warnings"),
    path("warnings_instance", views.warnings_instance, name = "warnings_instance"),
    path("metrics", views.metrics, name = "metrics"),
    path("retag", views.retag, name = "retag"),
] 

