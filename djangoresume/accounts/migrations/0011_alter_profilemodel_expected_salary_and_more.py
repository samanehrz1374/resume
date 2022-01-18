# Generated by Django 4.0 on 2022-01-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_profilemodel_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='Expected_Salary',
            field=models.IntegerField(null=True, verbose_name='حقوق درخواستی'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='address',
            field=models.CharField(max_length=300, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='birthday',
            field=models.DateField(null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='شهر محل سکونت'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='intrested_job',
            field=models.CharField(max_length=100, null=True, verbose_name='شغل مورد علاقه'),
        ),
    ]
