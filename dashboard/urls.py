from django.urls import include, path

from .views import BaseView

urlpatterns = [
    path("", BaseView.as_view(), name="dashboard_base"),
] 

