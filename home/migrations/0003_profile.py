# Generated by Django 3.0.9 on 2020-08-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200813_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backimg', models.ImageField(upload_to='pics')),
                ('proimg', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('desig', models.TextField()),
            ],
        ),
    ]