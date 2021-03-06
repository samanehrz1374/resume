from calendar import month_name
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from jalali_date import date2jalali
# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        verbose_name="profiles"
        verbose_name_plural="profiles"
    user=models.OneToOneField(User,on_delete=CASCADE,verbose_name="کاربری",related_name="profile")
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

  

class aducationModel(models.Model):
    class Meta:
        verbose_name="سوابق تحصیلی"
        verbose_name_plural="سوابق تحصیلی"
    aducations = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
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
    def __str__(self):
        return self.university


class workexperienceModel(models.Model):
    class Meta:
        verbose_name="سوابق شغلی"
        verbose_name_plural="سوابق شغلی"
    jobs = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    job_area=models.CharField(max_length=100,null=True,blank=True)
    job_title=models.CharField(max_length=100,verbose_name="عنوان شغل")
    company_name=models.CharField(max_length=100,verbose_name="نام شرکت")
    start_time=models.DateField(verbose_name="تاریخ شروع",null=True)
    end_time=models.DateField(verbose_name="تاریخ پایان",null=True)

    def __str__(self):
        return self.job_title

    
class skillsModel(models.Model):
    class Meta:
        verbose_name="مهارت ها"
        verbose_name_plural="مهارت ها"
    skills = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    #skill_area=models.CharField(max_length=100,null=True,verbose_name="حوزه کاری")
    skillname=models.CharField(max_length=100,verbose_name="مهارت")
    Basic=1
    intermidiate=2
    advanced=3
    status_choices=((Basic,"مقدماتی"),
                    (intermidiate,"متوسط"),
                    (advanced,"پیشرفته"))
    levelofskill=models.IntegerField(choices=status_choices,verbose_name="سطح مهارت",null=True)

    def __str__(self):
        return self.skillname
    

class coursesModel(models.Model):
    class Meta:
        verbose_name="دوره های آموزشی"
        verbose_name_plural="دوره های آموزشی"
    courses=models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    coursesname=models.CharField(max_length=300,verbose_name="نام دوره آموزشی")
    institute=models.CharField(max_length=300,verbose_name="نام آموزشگاه")
    certificate=models.URLField(null=True,blank=True)


    def __str__(self):
        return self.coursesname



class languagesModel(models.Model):
    class Meta:
        verbose_name="زبان ها"
        verbose_name_plural="زبان ها"
    languages=models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
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


class awardsModel(models.Model):
    class Meta:
        verbose_name="جوایزو افتخارات"
        verbose_name_plural="جوایزو افتخارات"
    awards=models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    award_title=models.CharField(max_length=300,verbose_name="عنوان")
    dateofaward=models.DateField(verbose_name="سال")

    def __str__(self):
        return self.award_title


class projectsModel(models.Model):
    class Meta:
        verbose_name="پروژه ها و تجربیات آکادمیک"
        verbose_name_plural="پروژه ها و تجربیات آکادمیک"
    projects=models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    project_title=models.CharField(max_length=300,verbose_name="عنوان")
    dateofproject=models.DateField(verbose_name="سال",null=True)

    def __str__(self):
        return self.project_title

class articlesModel(models.Model):
    class Meta:
        verbose_name="کتاب ها و مقالات"
        verbose_name_plural="کتاب ها و مقالات"
    articles=models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    article_title=models.CharField(max_length=500,verbose_name="عنوان")
    dateofarticle=models.DateField(verbose_name="سال",null=True)

    def __str__(self):
        return self.article_title