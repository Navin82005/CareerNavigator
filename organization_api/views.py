from django.shortcuts import render, redirect
import csv, openpyxl, re
from datetime import datetime
from .models import Organization, OrganizationData
from .serializers import *

# Create your views here.
def UploadXLFile(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login/')

    return render(request, "profile/organization.html")
    

def ParseXLFile(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login/')

    if request.method == 'POST':
        file_ = request.FILES["file"]
        headers = request.POST.get('headers')

        headers = headers.split(',')
        for i in range(len(headers)):
            headers[i] = headers[i].strip()

        print(headers)

        user = request.user
        organization = Organization.objects.get(user=user)
        
        try:
            orgData = OrganizationData.objects.get(organization=organization)
            orgData.studentsDataFile = file_
            orgData.save()
        
        except Exception as e:
            if str(e).lower() == "OrganizationData matching query does not exist.".lower():
                newOrgData = OrganizationData.objects.create(organization=organization)
                newOrgData.studentsDataFile = file_
                newOrgData.save()

        fileParser = XlsxFileParser(file_)
        formattedData = fileParser.parseXlsxFile()

        accountSerializer = CreateAccounts(formattedData)
        accountSerializer.create_accounts(headers)

        return render(request, "profile/organization.html")


def ProfileView(request, id):

    if not request.user.is_authenticated:
        return redirect(f"/auth/login/?redirect=organization/profile/{id}")

    return render(request, "profile/orgprofile.html")
