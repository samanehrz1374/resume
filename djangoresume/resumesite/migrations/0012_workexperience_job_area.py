# Generated by Django 4.0 on 2022-02-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0011_aboutmemodel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='job_area',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
