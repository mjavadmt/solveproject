from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="Index2"),
    path("chat", views.show_chat, name="show_chat"),
    path("appendchat", views.save_text, name="append_chat")

]
