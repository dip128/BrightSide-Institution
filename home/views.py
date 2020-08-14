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

