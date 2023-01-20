from django.urls import path

from deals.apps.processor.api.v1.views.top_clients import TopClientsView
from deals.apps.processor.api.v1.views.uplaod_csv import UploadCSV

urlpatterns = [
    path("topic-clients/", TopClientsView.as_view(), name="topic_clients"),
    path("upload-csv/", UploadCSV.as_view(), name="upload_csv"),
]
