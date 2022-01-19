from django import forms
from accounts.models import ProfileModel



class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model=ProfileModel
        fields=['profileimage','gender']
    
        # Widget={
        #     'gender':forms.CharField(widget=forms.Select(attrs={'class': "form-control"}))

        # }