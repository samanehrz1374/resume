from dataclasses import fields
from django import forms
from accounts.models import ProfileModel
from django.contrib.auth.forms import UserChangeForm






class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,error_messages={'required':"enter"})
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput) 
    email = forms.CharField(widget=forms.EmailInput)
    ProfileImage=forms.ImageField(required=False)
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender']
    def clean(self):
        cleaned_data = super(ProfileRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError("raise an error")
           




class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender','marital_status','city','address','birthday','intrested_job']          



class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=['first_name','last_name','email']
    password=None