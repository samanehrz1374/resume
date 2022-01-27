# Generated by Django 4.0 on 2022-01-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_profilemodel_degree_level_profilemodel_from_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='article_title',
            field=models.CharField(max_length=500, null=True, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='award_title',
            field=models.CharField(max_length=300, null=True, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='company_name',
            field=models.CharField(max_length=100, null=True, verbose_name='نام شرکت'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='coursesname',
            field=models.CharField(max_length=300, null=True, verbose_name='نام دوره آموزشی'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='dateofarticle',
            field=models.TimeField(null=True, verbose_name='سال'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='dateofaward',
            field=models.TimeField(null=True, verbose_name='سال'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='dateofproject',
            field=models.TimeField(null=True, verbose_name='سال'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='تاریخ پایان'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='institute',
            field=models.CharField(max_length=300, null=True, verbose_name='نام آموزشگاه'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='job_title',
            field=models.CharField(max_length=100, null=True, verbose_name='عنوان شغل'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='language',
            field=models.CharField(max_length=100, null=True, verbose_name='زبان'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='leveloflanguage',
            field=models.IntegerField(choices=[(1, 'مقدماتی'), (2, 'پایین تر از متوسط'), (3, 'متوسط'), (4, 'بالاتر از متوسط'), (5, 'پیشرفته'), (6, 'زبان مادری')], null=True, verbose_name='سطح مهارت'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='levelofskill',
            field=models.IntegerField(choices=[(1, 'مقدماتی'), (2, 'متوسط'), (3, 'پیشرفته')], null=True, verbose_name='سطح مهارت'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='project_title',
            field=models.CharField(max_length=300, null=True, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='skillname',
            field=models.CharField(max_length=100, null=True, verbose_name='مهارت'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='تاریخ شروع'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='major',
            field=models.CharField(max_length=100, null=True, verbose_name='رشته تحصیلی'),
        ),
    ]