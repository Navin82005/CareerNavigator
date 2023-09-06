from .models import *
from django.contrib.auth.models import User

import colorama
from colorama import Fore

colorama.init()


class ProfileSerializer:
    def __init__(self, id):
        self.id = id
        self.profile = Profile.objects.get(user=id)
    
    def getProjects(self):
        # print(f"{Fore.GREEN}" + "Profile = ", profile.name, "\033[0m")
        projects = self.profile.projects_works.all()
        data = []
        projects = list(projects)
        # print(f"{Fore.GREEN}", projects, "\033[0m", len(projects))
        for i in range(len(projects)):
            if (projects[i].images.all().count() == 0):
                continue
            data += [[projects[i], projects[i].images.all()[0]]]
        return data

    def getWorkExperience(self):
        data = {}
        year = self.profile.work_exp_year[1:-1].split('|')
        work = self.profile.work_exp_work[1:-1].split('|')
        length = len(work)
        for i in range(length):
            data[year[i]] = work[i]
        
        return data

    def getEducation(self):
        data = {}
        year = self.profile.educated_year[1:-1].split('|')
        university = self.profile.educated_university[1:-1].split('|')
        length = len(university)
        for i in range(length):
            data[year[i]] = university[i]

        return data

    def getSkills(self):
        data = self.profile.skill[1:-1].split('|')

        return data

    def getSocialLinks(self):
        raw_data = []

        raw_data += [self.profile.LinkedIn.split('|')]
        raw_data += [self.profile.twitter.split('|')]
        raw_data += [self.profile.github.split('|')]
        raw_data += [self.profile.codepen.split('|')]
        raw_data += [self.profile.youtube.split('|')]
        raw_data += [self.profile.facebook.split('|')]
        raw_data += [self.profile.instagram.split('|')]
        data = []

        for i in range(raw_data.count([''])):
            raw_data.remove([''])

        for i in raw_data:
            temp = {}
            temp['icon'] = i[0]
            temp['name'] = i[1]
            temp['url'] = i[2]
            data.append(temp)

        return data