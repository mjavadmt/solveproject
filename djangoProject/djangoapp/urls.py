from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
    path("logout", views.logoutuser, name="logout"),
    path("choosefremp", views.choosefremp, name="choosefremp"),
    path("Ali_esm_bezar", views.Ali_esm_bezar, name="Ali_esm_bezar")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
