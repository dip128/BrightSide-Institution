from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("course",views.course,name="course"),
    path("services",views.services,name="services"),
    path("about",views.about,name="about"),
    path("blog",views.blog,name="blog")

]
