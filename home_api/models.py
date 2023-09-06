from django.db import models
from organization_api.models import Organization


# Create your models here.
class HomeData(models.Model):
    serviceOfferings = models.CharField(max_length=10000, blank=True)
