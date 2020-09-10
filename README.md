# BrightSide-Institution
A Software service &amp; training institute website
A website for Software Training Institute Or a IT Service Stratup
[Demo](http://dip128.pythonanywhere.com/)
django_postgresql
using postgresql database with django

INSTALLATION
Install the postgresql database & pgadmin4 in your local computer first from the .exe file on the offical site.

Install the postgresql package for python - psycopg2 using pip in virtualenv

CONFIGURE
Create a new virtualenv and then install all the dependencies for our project there

Create a new django project

Create a new database using the postgresql command line Or by using pgadmin4 tool.

CREATE DATABASE BrightSide Institute

Inside our django project settings.py, set the database as the postgresql like so,
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BrightSide Institute' ,
        'USER':'postgres',
        'PASSWORD':'', #Your Password
        'HOST':'localhost'
    }
}
DJANGO USAGE
Just create models and run makemigrations and migrate command, then you are good to go..
