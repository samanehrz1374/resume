# Generated by Django 4.0 on 2022-03-08 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_alter_skillsmodel_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsmodel',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profilemodel'),
        ),
    ]
