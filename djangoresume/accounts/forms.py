from calendar import monthrange
from dataclasses import fields
from datetime import MINYEAR, datetime
from django import forms
from accounts.models import ProfileModel
from django.contrib.auth.forms import UserChangeForm
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget







class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,error_messages={'required':"enter"})
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput) 
    email = forms.CharField(widget=forms.EmailInput)
    # ProfileImage=forms.ImageField(required=True)
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender']
    def clean(self):
        cleaned_data = super(ProfileRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError("raise an error")
           


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