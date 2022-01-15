from ast import mod
from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل"
    firstname=models.CharField(max_length=100,verbose_name="نام")
    lastname=models.CharField(max_length=100,verbose_name="نام خانوادگی")
    male=1
    female=2
    status_choices=((male,"مرد"),(female,"زن"))
    gender=models.IntegerField(choices=status_choices,verbose_name="جنسیت")
    single=1
    married=2
    status_choices1=((single,"مجرد"),(married,"متاهل"))
    marital_status=models.IntegerField(choices=status_choices1,verbose_name="وضعیت تاهل")
    city=models.CharField(max_length=100,verbose_name="شهر محل سکونت")
    address=models.CharField(max_length=300,verbose_name="آدرس")
    birthday=models.DateField(verbose_name="تاریخ تولد")
    Expected_Salary=models.IntegerField(verbose_name="حقوق درخواستی")
    intrested_job=models.CharField(max_length=100,verbose_name="شغل مورد علاقه")

    def __str__(Self):
        return Self.name

    
