# Generated by Django 4.0 on 2022-02-25 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_alter_articlesmodel_dateofarticle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesmodel',
            name='dateofarticle',
        ),
        migrations.RemoveField(
            model_name='awardsmodel',
            name='award_title',
        ),
        migrations.RemoveField(
            model_name='awardsmodel',
            name='dateofaward',
        ),
        migrations.RemoveField(
            model_name='projectsmodel',
            name='dateofproject',
        ),
    ]
