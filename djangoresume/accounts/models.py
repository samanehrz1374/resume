from ast import mod
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل"
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="کاربری",related_name="profile",null=True)
    # firstname=models.CharField(max_length=100,verbose_name="نام")
    # lastname=models.CharField(max_length=100,verbose_name="نام خانوادگی")
    male=1
    female=2
    status_choices=((male,"مرد"),(female,"زن"))
    gender=models.IntegerField(choices=status_choices,verbose_name="جنسیت",null=True)
    single=1
    married=2
    status_choices1=((single,"مجرد"),(married,"متاهل"))
    marital_status=models.IntegerField(choices=status_choices1,verbose_name="وضعیت تاهل",null=True)
    city=models.CharField(max_length=100,verbose_name="شهر محل سکونت",null=True)
    address=models.CharField(max_length=300,verbose_name="آدرس",null=True)
    birthday=models.DateField(verbose_name="تاریخ تولد",null=True)
    Expected_Salary=models.IntegerField(verbose_name="حقوق درخواستی",null=True)
    intrested_job=models.CharField(max_length=100,verbose_name="شغل مورد علاقه",null=True)
    profileimage=models.ImageField(upload_to='profileimages/',null=True)

    def __str__(Self):
        return Self.name

    
