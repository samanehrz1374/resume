# Generated by Django 4.0 on 2022-01-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_profilemodel_article_title_profilemodel_award_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='skillname',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='مهارت'),
        ),
    ]
