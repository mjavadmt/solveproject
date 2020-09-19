from django.urls import path
from . import views

urlpatterns = [
    path("", views.first_page, name="first_page"),
    path("chat", views.show_chat, name="show_chat"),
    path("appendchat", views.save_text, name="append_chat")

]
