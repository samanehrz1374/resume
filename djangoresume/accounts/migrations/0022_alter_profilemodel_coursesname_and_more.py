# Generated by Django 4.0 on 2022-01-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_profilemodel_skillname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='coursesname',
            field=models.CharField(default='aaa', max_length=300, null=True, verbose_name='نام دوره آموزشی'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='skillname',
            field=models.CharField(max_length=100, null=True, verbose_name='مهارت'),
        ),
    ]
