# Generated by Django 4.0 on 2022-02-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0010_aboutmemodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmemodel',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
