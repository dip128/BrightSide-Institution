from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("course",views.course,name="course"),
    path("services",views.services,name="services"),
    path("about",views.about,name="about"),
    path("blog",views.blog,name="blog"),
    path("contact",views.contact,name="contact"),
    path("FreeCourses",views.freecourse,name="freecourse"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("signup",views.signup,name="signup")
]
