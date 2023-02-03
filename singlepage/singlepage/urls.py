from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("episodes/", views.index, name="episodes"),
    path("bios/", views.index, name="bios"),
    path("contact/", views.index, name="contact"),
]