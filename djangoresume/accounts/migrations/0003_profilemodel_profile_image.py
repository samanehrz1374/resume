# Generated by Django 4.0 on 2022-01-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_requested_rights_profilemodel_expected_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profileimages/'),
        ),
    ]
