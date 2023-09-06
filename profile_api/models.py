from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, to_field='id', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    develop_typed = models.CharField(max_length=655, blank=True, default='[]')
    image = models.ImageField(blank=True, upload_to='images/profile',)
    # Bio Data of user
    dob = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    # Work Experience 
    work_exp_year = models.CharField(max_length=625, blank=True, default='[]')
    work_exp_work = models.CharField(max_length=625, blank=True, default='[]')

    # Education Qualifications
    educated_year = models.CharField(max_length=625, blank=True, default='[]')
    educated_university = models.CharField(max_length=625, blank=True, default='[]')

    # Skills
    skill = models.CharField(max_length=625, blank=True, default='[]')

    # Contact Information
    LinkedIn = models.CharField(max_length=225, blank=True)
    twitter = models.CharField(max_length=225, blank=True)
    github = models.CharField(max_length=225, blank=True)
    codepen = models.CharField(max_length=225, blank=True)
    youtube = models.CharField(max_length=225, blank=True)
    facebook = models.CharField(max_length=225, blank=True)
    instagram = models.CharField(max_length=225, blank=True)


    # Link to projects
    projects_works = models.ManyToManyField('Projects', blank=True)

    def __str__(self):
        return str(self.name) + "'s Profile"

class ProjectImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images\profile\projects', null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Projects(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    images = models.ManyToManyField('ProjectImage')

    def __str__(self):
        return str(self.name)
