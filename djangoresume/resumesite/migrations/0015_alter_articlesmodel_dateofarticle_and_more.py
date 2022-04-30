# Generated by Django 4.0 on 2022-04-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0014_coursesmodel_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='dateofarticle',
            field=models.DateField(verbose_name='سال'),
        ),
        migrations.AlterField(
            model_name='awardsmodel',
            name='dateofaward',
            field=models.DateField(verbose_name='سال'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='job_title',
            field=models.CharField(max_length=300, verbose_name='عنوان شغل'),
        ),
    ]