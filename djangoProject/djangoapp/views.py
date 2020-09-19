from django.shortcuts import render
from django import forms
from django.http import *
from django.shortcuts import render
from django.urls import reverse
from .models import *


def first_page(request):
    return render(request, "djangoapp/firstpage.html")


def show_chat(request):
    return render(request, "djangoapp/chat.html", {
        "all_chats": Temp.objects.all()
    })


def save_text(request):
    if request.method == "POST":
        temp = Temp(message=request.POST["msg_ajax"])
        if temp.message is not None and temp is not None:
            temp.save()
        return HttpResponseRedirect(reverse("show_chat"))
    if request.method == "Get":
        return HttpResponseRedirect(reverse("show_chat"))
