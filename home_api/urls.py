from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomeView, name="HomeView"),
    path("organizations", OrganizationView, name="AboutView"),
    path("news", NewsView, name="NewsView"),
    path("blog", BlogView, name="BlogView"),
    path("about-us", AboutView, name="AboutView"),
]
