# Generated by Django 4.0 on 2022-01-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='profileimage',
            new_name='ProfileImage',
        ),
    ]
