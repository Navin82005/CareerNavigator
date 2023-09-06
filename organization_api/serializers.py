import openpyxl
from datetime import datetime
from django.contrib.auth.models import User
from profile_api.models import Profile

class XlsxFileParser:
    def __init__(self, filename):
        self.workbook = openpyxl.load_workbook(filename)

    def parseXlsxFile(self):
        sheet = self.workbook[self.workbook.sheetnames[0]]
        
        headings = []
        
        for head_object in sheet[1]:
            headings.append(head_object.value.lower())

        formattedData = {}
        for i in headings:
            formattedData[i] = []

        i = 0
        k = 0
        for cell in sheet:
            i = 0
            if k == 0:
                k += 1
                continue
            for data in cell:
                if str(data.value).lower() in headings:
                    continue
                
                if type(data.value) == datetime:
                    formattedData[headings[i]] += [data.value.strftime('%d-%m-%Y')]
                    i += 1
                    continue

                formattedData[headings[i]] += [data.value]
                i += 1
        self.workbook.close()
        return formattedData

class CreateAccounts:
    def __init__(self, data):
        self.data = data
    
    def create_accounts(self, fields):
        email = 'email'
        name = 'name'
        dob = 'dob'
        rno = 'rollno'

        errorData = []

        for i in range(len(self.data[name])):
            try:
                newuser = User.objects.create(username=self.data[name][i], email=self.data[email][i])
                newuser.save()
                newProfile = Profile.objects.create(user=newuser, name=newuser.username)
                newProfile.save()
            except Exception as e:
                if str(e)[:71] == 'duplicate key value violates unique constraint "auth_user_username_key"':
                    errorData += [self.data[name][i]]

        print(errorData)
    