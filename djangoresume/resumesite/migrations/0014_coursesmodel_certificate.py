# Generated by Django 4.0 on 2022-02-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0013_skillsmodel_skill_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesmodel',
            name='certificate',
            field=models.URLField(blank=True, null=True),
        ),
    ]