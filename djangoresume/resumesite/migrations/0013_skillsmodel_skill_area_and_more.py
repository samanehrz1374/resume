# Generated by Django 4.0 on 2022-02-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0012_workexperience_job_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillsmodel',
            name='skill_area',
            field=models.CharField(max_length=100, null=True, verbose_name='حوزه کاری'),
        ),
        migrations.AlterField(
            model_name='aducationmodel',
            name='degree_level',
            field=models.IntegerField(choices=[(1, 'Associate'), (2, 'Bachelor of science'), (3, 'Master of science '), (4, 'phD')], verbose_name='مقطع تحصیلی'),
        ),
        migrations.AlterField(
            model_name='aducationmodel',
            name='major',
            field=models.CharField(max_length=100, verbose_name='رشته تحصیلی'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='job_area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
