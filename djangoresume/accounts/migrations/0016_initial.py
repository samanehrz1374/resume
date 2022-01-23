# Generated by Django 4.0 on 2022-01-22 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0015_delete_profilemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], null=True, verbose_name='جنسیت')),
                ('marital_status', models.IntegerField(choices=[(1, 'مجرد'), (2, 'متاهل')], null=True, verbose_name='وضعیت تاهل')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='شهر محل سکونت')),
                ('address', models.CharField(max_length=300, null=True, verbose_name='آدرس')),
                ('birthday', models.DateField(null=True, verbose_name='تاریخ تولد')),
                ('Expected_Salary', models.IntegerField(null=True, verbose_name='حقوق درخواستی')),
                ('intrested_job', models.CharField(max_length=100, null=True, verbose_name='شغل مورد علاقه')),
                ('profileimage', models.ImageField(upload_to='profileimages/', verbose_name='عکس')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user', verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل',
            },
        ),
    ]