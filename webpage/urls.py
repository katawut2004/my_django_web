from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.indexPage),
    path("about/", views.aboutUs),
    path("contact/", views.contactUs),
]
