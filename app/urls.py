from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.UploadList.as_view(), name='upload_list'),
    path('download/<int:pk>/', views.download, name='download'),  # this is for download view
    path('download/zip/', views.download_zip, name='download_zip'),  # this is for download_zip
]