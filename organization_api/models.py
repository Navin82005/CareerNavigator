from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=2555)
    startDate = models.CharField(max_length=20)
    eventType = models.CharField(max_length=30, blank=True)
    image = models.ImageField(blank=True, upload_to="organization/events")
    content = models.CharField(blank=True, max_length=2555)
    applications = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return str(self.title)


class Organization(models.Model):
    user = models.OneToOneField(User, to_field="id", on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    organizationType = models.CharField(max_length=225)
    image = models.ImageField(blank=True, upload_to="organization")
    events = models.ManyToManyField(Events, related_name="organization")

    def __str__(self):
        return str(self.name)


class OrganizationData(models.Model):
    organization = models.OneToOneField(
        Organization, to_field="id", on_delete=models.CASCADE
    )
    studentsDataFile = models.FileField(blank=True, upload_to="organization/dataFiles")

    def __str__(self):
        return str(self.organization)
