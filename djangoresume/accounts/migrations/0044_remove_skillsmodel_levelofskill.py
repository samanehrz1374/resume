# Generated by Django 4.0 on 2022-03-05 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_awardsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillsmodel',
            name='levelofskill',
        ),
    ]