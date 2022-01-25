from calendar import monthrange
from dataclasses import fields
from datetime import MINYEAR, datetime
from django import forms
from accounts.models import ProfileModel
from django.contrib.auth.forms import UserChangeForm
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget







class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10,required=True,label="نام")
    last_name = forms.CharField(max_length=10,required=True,label=" نام خانوادگی")
    username = forms.CharField(max_length=10,min_length=3,help_text="نام کاربری باید 3 تا 10 کلمه باشد و از علامت های _ @ - استفاده نشود",required=True,label=" نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput,help_text="رمز عبور شامل حروف بزرگ و کوچک و اعداد باشد",required=True,label="رمز عبور")
    confirm_password = forms.CharField(widget=forms.PasswordInput,required=True,label="تکرار رمز عبور") 
    email = forms.CharField(widget=forms.EmailInput,required=True,label="ایمیل")
    ProfileImage=forms.ImageField(required=False, label="تصویر پروفایل")
    required_css_class = 'required'
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender']
    def clean(self,*args, **kwargs):
        
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")

        if password != confirm:
           self.add_error('confirm_password', "!تکرار کلمه عبود با کلمه عبور برابر نیست")
        
           


YEAR_CHOICES = range(1400, 1300, -1)
MONTH_CHOICES = {1: 'فروردین',2: 'اردیبهشت',3: 'خرداد',4: 'تیر',5: 'مرداد',6: 'شهریور',7: 'مهر',8: 'آبان',9: 'آذر',10: 'دی',11: 'بهمن',12: 'اسفند'}


class ProfileEditForm(forms.ModelForm):
    ProfileImage=forms.ImageField(widget=forms.FileInput,)
    # birthday=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender','marital_status','city','address','birthday','intrested_job']          
    
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields["birthday"] = forms.DateField(required=False, widget=forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES))
        

        


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=['first_name','last_name','email']
    password=None