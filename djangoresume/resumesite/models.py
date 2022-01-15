from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class aboutmeModel(models.Model):
    class Meta:
        verbose_name="درباره من"
        verbose_name_plural="درباره من"
    Name=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Name

class aducationModel(models.Model):
    class Meta:
        verbose_name="سوابق تحصیلی"
        verbose_name_plural="سوابق تحصیلی"
    Associate=1
    Bachelor=2
    Master=3
    phD=4
    status_choices=((Associate,"کاردانی"),
                    (Bachelor,"کارشناسی"),
                    (Master,"کارشناسی ارشد"),
                    (phD,"دکترا"))
    degree_level=models.IntegerField(choices=status_choices,verbose_name="مقطع تحصیلی")
    major=models.CharField(max_length=100,verbose_name="مقطع تحصیلی")
    university=models.CharField(max_length=100,verbose_name="دانشگاه")
    gpa=models.FloatField(verbose_name="معدل")
    from_year=models.DateField(verbose_name="سال شروع")
    to_year=models.DateField(verbose_name="سال پایان")

    def __str__(self):
        return self.degree_level


class workexperience(models.Model):
    class Meta:
        verbose_name="سوابق شغلی"
        verbose_name_plural="سوابق شغلی"
    job_title=models.CharField(max_length=100,verbose_name="عنوان شغل")
    company_name=models.CharField(max_length=100,verbose_name="نام شرکت")
    start_time=models.TimeField(verbose_name="تاریخ شروع")
    end_time=models.TimeField(verbose_name="تاریخ پایان")

    def __str__(self):
        return self.job_title


class languagesModel(models.Model):
    class Meta:
        verbose_name="زبان ها"
        verbose_name_plural="زبان ها"
    language=models.CharField(max_length=100,verbose_name="زبان")
    Basic=1
    preintermidiate=2
    intermidiate=3
    upperintermidiate=4
    advanced=5
    native=6
    status_choices=((Basic,"مقدماتی"),
                    (preintermidiate,"پایین تر از متوسط"),
                    (intermidiate,"متوسط"),
                    (upperintermidiate,"بالاتر از متوسط"),
                    (advanced,"پیشرفته"),
                    (native,"زبان مادری"),
                    )
    leveloflanguage=models.IntegerField(choices=status_choices,verbose_name="سطح مهارت")

    def __str__(self):
        return self.language

class skillsModel(models.Model):
    class Meta:
        verbose_name="مهارت ها"
        verbose_name_plural="مهارت ها"
    skillname=models.CharField(max_length=100,verbose_name="مهارت")
    Basic=1
    intermidiate=2
    advanced=3
    status_choices=((Basic,"مقدماتی"),
                    (intermidiate,"متوسط"),
                    (advanced,"پیشرفته"))
    levelofskill=models.IntegerField(choices=status_choices,verbose_name="سطح مهارت")

    def __str__(self):
        return self.skillname

class coursesModel(models.Model):
    class Meta:
        verbose_name="دوره های آموزشی"
        verbose_name_plural="دوره های آموزشی"
    coursesname=models.CharField(max_length=300,verbose_name="نام دوره آموزشی")
    institute=models.CharField(max_length=300,verbose_name="نام آموزشگاه")


    def __str__(self):
        return self.coursesname

class awardsModel(models.Model):
    class Meta:
        verbose_name="جوایزو افتخارات"
        verbose_name_plural="جوایزو افتخارات"
    award_title=models.CharField(max_length=300,verbose_name="عنوان")
    dateofaward=models.TimeField(verbose_name="سال")

    def __str__(self):
        return self.award_title


class projectsModel(models.Model):
    class Meta:
        verbose_name="پروژه ها و تجربیات آکادمیک"
        verbose_name_plural="پروژه ها و تجربیات آکادمیک"
    project_title=models.CharField(max_length=300,verbose_name="عنوان")
    dateofproject=models.TimeField(verbose_name="سال")

    def __str__(self):
        return self.project_title

class articlesModel(models.Model):
    class Meta:
        verbose_name="کتاب ها و مقالات"
        verbose_name_plural="کتاب ها و مقالات"
    article_title=models.CharField(max_length=500,verbose_name="عنوان")
    dateofarticle=models.TimeField(verbose_name="سال")

    def __str__(self):
        return self.article_title