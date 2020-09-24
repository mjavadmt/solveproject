from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="Index2"),
    path("chat", views.show_chat, name="show_chat"),
    path("appendchat", views.save_text, name="append_chat"),
    path("contact",views.contact, name="contact"),
    path("element", views.element,name="element"),
    path("portfolio",views.portfolio,name= "portfolio"),
    path("price",views.price, name = "price"),
    path("services",views.services,name="services")

]
