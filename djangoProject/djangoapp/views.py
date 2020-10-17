from django.shortcuts import render
from django import forms
from django.http import *
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
# from django.utils import simplejson
from django.core import serializers



def Index(request):
    return render(request, "djangoapp/home.html")


def enterance(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    u = User.objects.get(id=request.user.id)
    if not u.is_staff:
        return render(request, "djangoapp/choosefremp.html")

    return render(request, "djangoapp/enterance.html")


def choosefremp(request):
    if request.method == "POST":
        get_type = request.POST['user_type']
        u = User.objects.get(id=request.user.id)
        u.is_staff = True
        u.save()
        if get_type == "freelancer":
            created_freelancer = Freelancer(user=u)
            created_freelancer.save()
        elif get_type == "employer":
            created_employer = Employer(user=u)
            created_employer.save()
        return HttpResponseRedirect(reverse('enterance'))

    return render(request, "djangoapp/choosefremp.html")


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        # user_type = request.POST["person"]
        get_list_username = list(User.objects.values_list("username"))
        get_list_password = list(User.objects.values_list("password"))
        for i in range(len(get_list_username)):
            get_list_username[i] = get_list_username[i][0]
        for i in range(len(get_list_password)):
            get_list_password[i] = get_list_password[i][0]
        if username in get_list_username or password in get_list_password:
            return render(request, "djangoapp/formsign.html", {"message": "PICK ANOTHER USERNAME AND PASSWORD"})
        created_user = User.objects.create_user(username=username, password=password, email=email)
        # if user_type == "freelancer":
        #     created_freelancer = Freelancer(user=created_user)
        #     created_freelancer.save()
        # else:
        #     created_employer = Employer(user=created_user)
        #     created_employer.save()
        # user = authenticate(request, username=username, password=password)
        # login(request, created_user)
        login(request, created_user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse("enterance"))


def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("enterance"))
        else:
            return render(request, "djangoapp/formsign.html", {"message": "Invalid credinatial"})
    return render(request, "djangoapp/formsign.html")


def logoutuser(request):
    logout(request)
    return render(request, "djangoapp/formsign.html", {"message": "logged out"})


def contact(request):
    return render(request, "djangoapp/contact.html")


def elements(request):
    return render(request, "djangoapp/elements.html")


def portfolio(request):
    return render(request, "djangoapp/portfolio.html")


def formsign(request):
    return render(request, "djangoapp/formsign.html")


def services(request):
    return render(request, "djangoapp/services.html")


def about(request):
    return render(request, "djangoapp/about.html")


def show_chat(request):
    return render(request, "djangoapp/chat.html", {
        "all_chats": Temp.objects.all()
    })


def Projectpage(request):
    projects = list(Project.objects.all())
    json_projects = serializers.serialize('json', projects,use_natural_foreign_keys=True)
    categories = Category.objects.all()
    dict_related_subjects_with_category = {}
    for category in categories:
        dict_related_subjects_with_category[category.name] = [i[0] for i in list(category.related_subjects.values_list("subject"))]
    return render(request, "djangoapp/projectpage.html",
                  {
                    "dict_items": dict_related_subjects_with_category,
                    "projects": json_projects
                  })


def save_text(request):
    if request.method == "POST":
        temp = Temp(message=request.POST["msg_ajax"])
        if temp.message is not None and temp is not None:
            temp.save()
        return HttpResponseRedirect(reverse("show_chat"))
    if request.method == "Get":
        return HttpResponseRedirect(reverse("show_chat"))
