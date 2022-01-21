from django import forms
from accounts.models import ProfileModel






class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,error_messages={'required':"enter"})
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput) 
    email = forms.CharField(widget=forms.EmailInput)
    profileimage=forms.ImageField(required=False)
    class Meta:
        model=ProfileModel
        fields=['profileimage','gender']
    def clean(self):
        cleaned_data = super(ProfileRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise self.ValidationError(
                "password and confirm_password does not match"
            )
   