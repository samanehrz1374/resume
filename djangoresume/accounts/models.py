from calendar import month_name
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from jalali_date import date2jalali
# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل"
    user=models.OneToOneField(User,on_delete=CASCADE,verbose_name="کاربری",related_name="profile")
    # firstname=models.CharField(max_length=100,verbose_name="نام")
    # lastname=models.CharField(max_length=100,verbose_name="نام خانوادگی")
    male=1
    female=2
    status_choices=((male,"مرد"),(female,"زن"))
    gender=models.IntegerField(choices=status_choices,verbose_name="جنسیت",null=True)
    single=1
    married=2
    status_choices1=((single,"مجرد"),(married,"متاهل"))
    marital_status=models.IntegerField(choices=status_choices1,verbose_name="وضعیت تاهل",null=True,blank=False)
    city=models.CharField(max_length=100,verbose_name="شهر محل سکونت",null=True,blank=False)
    address=models.CharField(max_length=300,verbose_name="آدرس",null=True,blank=False)
    birthday=models.DateField(verbose_name="تاریخ تولد",null=True,blank=False)
    Expected_Salary=models.IntegerField(verbose_name="حقوق درخواستی",null=True,blank=False)
    intrested_job=models.CharField(max_length=100,verbose_name="شغل مورد علاقه",null=True,blank=False)
    ProfileImage=models.ImageField(upload_to='profileimages/',verbose_name="عکس")

    Associate=1
    Bachelor=2
    Master=3
    phD=4
    status_choices2=((Associate,"کاردانی"),
                    (Bachelor,"کارشناسی"),
                    (Master,"کارشناسی ارشد"),
                    (phD,"دکترا"))
    degree_level=models.IntegerField(choices=status_choices2,verbose_name="مقطع تحصیلی",null=True)
    major=models.CharField(max_length=100,verbose_name="رشته تحصیلی",null=True)
    university=models.CharField(max_length=100,verbose_name="دانشگاه",null=True)
    gpa=models.FloatField(verbose_name="معدل",null=True)
    from_year=models.DateField(verbose_name="سال شروع",null=True)
    to_year=models.DateField(verbose_name="سال پایان",null=True)
    job_title=models.CharField(max_length=100,verbose_name="عنوان شغل",null=True)
    company_name=models.CharField(max_length=100,verbose_name="نام شرکت",null=True)
    start_time=models.DateField(verbose_name="تاریخ شروع",null=True)
    end_time=models.DateField(verbose_name="تاریخ پایان",null=True)
    language=models.CharField(max_length=100,verbose_name="زبان",null=True)
    Basic=1
    preintermidiate=2
    intermidiate=3
    upperintermidiate=4
    advanced=5
    native=6
    status_choices3=((Basic,"مقدماتی"),
                    (preintermidiate,"پایین تر از متوسط"),
                    (intermidiate,"متوسط"),
                    (upperintermidiate,"بالاتر از متوسط"),
                    (advanced,"پیشرفته"),
                    (native,"زبان مادری"),
                    )
    leveloflanguage=models.IntegerField(choices=status_choices3,verbose_name="سطح مهارت",null=True)
    skillname=models.CharField(max_length=100,verbose_name="مهارت",null=True)
    Basic=1
    intermidiate=2
    advanced=3
    status_choices4=((Basic,"مقدماتی"),
                    (intermidiate,"متوسط"),
                    (advanced,"پیشرفته"))
    levelofskill=models.IntegerField(choices=status_choices4,verbose_name="سطح مهارت",null=True)
    coursesname=models.CharField(max_length=300,verbose_name="نام دوره آموزشی",null=True)
    institute=models.CharField(max_length=300,verbose_name="نام آموزشگاه",null=True)
    award_title=models.CharField(max_length=300,verbose_name="عنوان",null=True)
    dateofaward=models.DateField(verbose_name="سال",null=True)
    project_title=models.CharField(max_length=300,verbose_name="عنوان",null=True)
    dateofproject=models.DateField(verbose_name="سال",null=True)
    article_title=models.CharField(max_length=500,verbose_name="عنوان",null=True)
    dateofarticle=models.DateField(verbose_name="سال",null=True)


    
