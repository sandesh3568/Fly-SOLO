from django.contrib import admin
from django.urls import path,include
from newapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("tracker",views.tracker,name="tracker"),
    path("login",views.login,name="login")
]