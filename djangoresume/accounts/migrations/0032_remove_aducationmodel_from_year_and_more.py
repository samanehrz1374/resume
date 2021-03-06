# Generated by Django 4.0 on 2022-02-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_remove_profilemodel_aducation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aducationmodel',
            name='from_year',
        ),
        migrations.RemoveField(
            model_name='aducationmodel',
            name='to_year',
        ),
        migrations.AddField(
            model_name='aducationmodel',
            name='from_yearr',
            field=models.IntegerField(null=True, verbose_name='سال شروع'),
        ),
        migrations.AddField(
            model_name='aducationmodel',
            name='to_yearr',
            field=models.IntegerField(null=True, verbose_name='سال پایان'),
        ),
        migrations.AlterField(
            model_name='aducationmodel',
            name='degree_level',
            field=models.IntegerField(choices=[(1, 'کاردانی'), (2, 'کارشناسی'), (3, 'کارشناسی ارشد'), (4, 'دکترا')], null=True, verbose_name='مقطع تحصیلی'),
        ),
        migrations.AlterField(
            model_name='aducationmodel',
            name='gpa',
            field=models.FloatField(null=True, verbose_name='معدل'),
        ),
        migrations.AlterField(
            model_name='aducationmodel',
            name='major',
            field=models.CharField(max_length=100, null=True, verbose_name='رشته تحصیلی'),
        ),
        migrations.AlterField(
            model_name='aducationmodel',
            name='university',
            field=models.CharField(max_length=100, null=True, verbose_name='دانشگاه'),
        ),
    ]
