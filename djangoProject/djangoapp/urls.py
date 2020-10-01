from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="Index2"),
    path("chat", views.show_chat, name="show_chat"),
    path("appendchat", views.save_text, name="append_chat"),
    path("contact", views.contact, name="contact"),
    path("elements", views.elements, name="elements"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("formsign", views.enterance, name="formsign"),
    path("services", views.services, name="services"),
    path("about", views.about, name="about"),
    path("projectpage", views.Projectpage, name="projectpage"),
    path("enterance", views.enterance, name="enterance"),
    path("signup", views.sign_up, name="signup"),
    path("login", views.loginuser, name="login"),
    path("logout", views.logoutuser, name="logout")
]
