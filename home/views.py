from django.shortcuts import render,HttpResponse
from .models import Service,Profile
# Create your views here.

def index(request):
    return render(request,'index.html')

def course(request):
    return render(request,'course.html')    
def about(request):
    return render(request,'about.html')  

def blog(request):
    return render(request,'blog.html')   

def services(request):
    servs = Service.objects.all()
    profls=Profile.objects.all()
    return render(request,'services.html',{'servs':servs,'profls':profls})       

def contact(request):
    return render(request,'contact.html')

def freecourse(request):
    return render(request,'freecourse.html')  

def login(request):
    return render(request,'login.html')      
def signup(request):
    return render(request,'signup.html')    