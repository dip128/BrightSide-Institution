# Generated by Django 3.0.9 on 2020-09-08 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
