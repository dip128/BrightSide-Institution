from django.shortcuts import render,HttpResponse
from .models import Service,Profile
from django.core.mail import send_mail
from django.contrib import messages

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
    if request.method=="POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']
        send_mail(
                 message_name,
                 message + '\n The Phone number is - '+ message_phone +'\n The Mail is - ' + message_email,
                 message_email,
                 ['brightside633@gmail.com'],
        )
        return render(request,'contact.html',{'message_name':message_name})
        messages.success(request, 'Your Mail has been sent.We will contact you as soon as possible.')
    else:    
        return render(request,'contact.html')

def freecourse(request):
    return render(request,'freecourse.html')  

def login(request):
    return render(request,'login.html')      
def signup(request):
    return render(request,'signup.html')    