# Generated by Django 4.0 on 2022-01-15 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0003_profilemodel_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user', verbose_name='کاربری'),
        ),
    ]
