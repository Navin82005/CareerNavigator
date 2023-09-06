from django.shortcuts import render
from .serializers import *

# Create your views here.
def HomeView(request):
    eventSerializer = EventSerializer(request.user.id)
    events = eventSerializer.getEvents()


    return render(request, "index.html", {"events": events})

def OrganizationView(request):
    return render(request, "organization.html")

def NewsView(request):
    return render(request, "news.html")

def BlogView(request):
    return render(request, "blog.html")

def AboutView(request):
    return render(request, "about.html")