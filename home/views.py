from django.shortcuts import render,HttpResponse,redirect
from .models import Service,Profile,Courses,Contacts
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def index(request):
    return render(request,'index.html')

def course(request):
    courses=Courses.objects.all()
    servs = Service.objects.all()
    return render(request,'course.html',{'servs':servs,'courses':courses})    
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
        name = request.POST.get('message-name',' ')
        email = request.POST.get('message-email',' ')
        phone = request.POST.get('message-phone',' ')
        messages = request.POST.get('message',' ')
        contacts = Contacts(name=name,email=email,phone=phone,messages=messages)
        contacts.save()
        return render(request,'contact.html',{'message_name':name})
        messages.success(request, 'Your Mail has been sent.We will contact you as soon as possible.')
    else:    
        return render(request,'contact.html')    
    '''
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

        '''
def freecourse(request):
    return render(request,'freecourse.html')  

def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invadlid Credentials")    
            return redirect('login')
    else:
        return render(request,'login.html') 
       
def signup(request):
    if request.method=="POST":
        first_name=request.POST['name']
        username=request.POST['email']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already Exsits')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'User created please login!')
                return redirect('login')
        else:
            messages.info(request,'Password Is not matching')
            return redirect('signup')
        
    else:
        return render(request,'signup.html')  


def logout(request):
    auth.logout(request)
    return redirect('/')