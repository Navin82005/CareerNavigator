from django.shortcuts import render, redirect
from .models import *
from .serializers import *

# Create your views here.
def ProfileView(request, id):
    try:
        profile = Profile.objects.get(user=id)
        user = User.objects.get(id=id)
    except Exception as e:
        return redirect(f'/organization/profile/{id}')

    first_name = user.first_name
    last_name = user.last_name

    profileSerializer = ProfileSerializer(id)

    project_works = profileSerializer.getProjects()
    work_experience = profileSerializer.getWorkExperience()
    education = profileSerializer.getEducation()
    skill = profileSerializer.getSkills()
    social_links = profileSerializer.getSocialLinks()

    profile_data = {"develops": profile.develop_typed[1:-1].split(",")}
    return render(
        request,
        "profile.html",
        {
            "profile": {
                "profile_data": profile_data,
                "profile": profile,
                "first_name": first_name,
                "last_name": last_name,
            },
            "project_works": project_works,
            "work_experience": work_experience,
            "education": education,
            "skills": skill,
            "social_links": social_links,
        },
    )
