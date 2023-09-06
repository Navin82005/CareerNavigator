from django.urls import path
from .views import *

urlpatterns = [
    path("upload/data/", UploadXLFile),
    path("upload/parse/data/", ParseXLFile),
    path("profile/<int:id>", ProfileView)
]