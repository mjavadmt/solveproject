from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *


def first_page(request):
    return render(request, "djangoapp/firstpage.html")
# Create your views here.
