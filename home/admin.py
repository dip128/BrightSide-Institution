from django.contrib import admin
from .models import Service,Profile,Courses,Contacts
# Register your models here.

admin.site.register(Service)
admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Contacts)