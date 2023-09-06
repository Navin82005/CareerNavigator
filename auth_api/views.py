from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from profile_api.models import Profile
from organization_api.models import Organization


# Create your views here.
def LoginView(request):
    try:
        redirect_url = '/' + request.GET.get("redirect")
    except Exception as e:
        redirect_url = None

    if request.user.is_authenticated:
        return redirect("/")

    return render(request, "authentications/login.html", {"redirect_url": redirect_url})


def authenticateLogin(request):
    print(request.GET.get("redirect"))
    if request.user.is_authenticated:
        return redirect("/")

    try:
        redirect_url = redirect(request.GET.get("redirect"))
    except Exception as e:
        redirect_url = None
        print(e)

    print(redirect_url)

    if request.method == "POST":
        email = request.POST.get("email")
        if "." in email and "@" in email:
            try:
                user = User.objects.get(email=email)
                password = request.POST.get("password")
                if user is not None or authenticate(
                    username=user.username, email=user.email, password=password
                ):
                    login(request, user)
                    return redirect_url or redirect("/")
                else:
                    return render(
                        request,
                        "authentications/login.html",
                        {
                            "error": {
                                "message": "Username or password is incorrect.",
                                "state": True,
                            },
                        },
                    )
            except Exception as e:
                if str(e).lower() == "User matching query does not exist.".lower():
                    return render(
                        request,
                        "authentications/login.html",
                        {
                            "error": {
                                "message": "Oops! It looks like you are new here.",
                                "state": True,
                            }
                        },
                    )
        else:
            try:
                username = request.POST.get("email")
                password = request.POST.get("password")
                if authenticate(username=username, password=password):
                    login(request, user)
                    return redirect("/")
                else:
                    return render(
                        request,
                        "authentications/login.html",
                        {
                            "error": {
                                "message": "Username or password is incorrect.",
                                "state": True,
                            }
                        },
                    )
            except Exception as e:
                if str(e).lower() == "User matching query does not exist.".lower():
                    return render(
                        request,
                        "authentications/login.html",
                        {
                            "error": {
                                "message": "Oops! It looks like you are new here.",
                                "state": True,
                            }
                        },
                    )
    else:
        return redirect("/")


def SignupView(request):
    if request.user.is_authenticated:
        return redirect("/")

    return render(request, "authentications/signup.html")


def authenticateRegister(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        rePassword = request.POST.get("reenterpassword")
        isOrg = request.POST.get("org")

        if User.objects.filter(email=email).exists():
            return render(
                request,
                "authentications/signup.html",
                {
                    "error": {
                        "message": "User account already exists.",
                        "state": "exists",
                    }
                },
            )
        else:
            if password != rePassword:
                data = {"name": username, "email": email}
                return render(
                    request,
                    "authentications/signup.html",
                    {
                        "error": {
                            "message": "Passwords doesn't match.",
                            "state": "wrongPassword",
                        },
                        "rerenderData": data,
                    },
                )

            else:
                newuser = User.objects.create(
                    username=username, password=password, email=email
                )
                newuser.save()
                user = User.objects.get(username=username, email=email)

                if isOrg:
                    newOrganization = Organization.objects.create(
                        user=user, name=username
                    )
                    newOrganization.save()
                else:
                    userprofile = Profile.objects.create(
                        user=user, name=username, email=email
                    )
                    userprofile.save()

                login(request, newuser)
            return redirect("/")

    else:
        return redirect("/")
