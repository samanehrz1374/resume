from calendar import monthrange
from dataclasses import fields
from datetime import MINYEAR, datetime
from django import forms
from accounts.models import ProfileModel,skillsModel,aducationModel,workexperienceModel,coursesModel,awardsModel,projectsModel,languagesModel,articlesModel
from django.contrib.auth.forms import UserChangeForm
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
import string
from django.forms.models import modelformset_factory,inlineformset_factory










class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10,required=True,label="نام")
    last_name = forms.CharField(max_length=10,required=True,label=" نام خانوادگی")
    username = forms.CharField(max_length=15,min_length=3,help_text="نام کاربری باید 3 تا 15 کلمه باشد و از علامت استفاده نشود",required=True,label=" نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput,help_text="رمز عبور شامل حروف بزرگ و کوچک و اعداد باشد",required=True,label="رمز عبور")
    confirm_password = forms.CharField(widget=forms.PasswordInput,required=True,label="تکرار رمز عبور") 
    email = forms.CharField(widget=forms.EmailInput,required=True,label="ایمیل")
    ProfileImage=forms.ImageField(required=False, label="تصویر پروفایل")
    required_css_class = 'required'
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender']
    def clean(self,*args, **kwargs):
        username =self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        SpecialSym =['$', '@', '#', '%']
        if password != confirm:
           self.add_error('confirm_password', "تکرار کلمه عبود با کلمه عبور برابر نیست!")
            
        for i in username:
            if i in string.punctuation:
                self.add_error('username', "نام کاربری نباید شامل علامت باشد!")

        if not any(char.isdigit() for char in password):
            self.add_error('password', "رمز عبور باید حداقل شامل یک عدد باشد")
            
            
          
        if not any(char.isupper() for char in password):
            self.add_error('password', "رمز عبور باید حداقل شامل یک حرف بزرگ باشد")
           
          
        if not any(char.islower() for char in password):
            self.add_error('password', "رمز عبور باید حداقل شامل یک حرف کوچک باشد")
            
          
        if not any(char in SpecialSym for char in password):
            self.add_error('password', "رمز عبور باید حداقل شامل یکی از علامت های @، %، $، # باشد")
            
                
            


YEAR_CHOICES = range(1400, 1300, -1)
MONTH_CHOICES = {1: 'فروردین',2: 'اردیبهشت',3: 'خرداد',4: 'تیر',5: 'مرداد',6: 'شهریور',7: 'مهر',8: 'آبان',9: 'آذر',10: 'دی',11: 'بهمن',12: 'اسفند'}


class ProfileEditForm(forms.ModelForm):
    ProfileImage=forms.ImageField(widget=forms.FileInput)
    # birthday=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=ProfileModel
        fields=['ProfileImage','gender','marital_status','city','address','birthday','intrested_job']          
    
    
    def __init__(self, *args, **kwargs):
    #         # first call parent's constructor
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        a=['ProfileImage','gender','marital_status','city','address','birthday','intrested_job']
    #         # there's a `fields` property now
        for key in a:
            self.fields[key].required = False  
        
        self.fields["birthday"] = forms.DateField(required=False, widget=forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES))
      


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=['first_name','last_name','email']
    password=None




class ResumeEditForm(forms.ModelForm):
    ProfileImage=forms.ImageField(widget=forms.FileInput)
    
    class Meta:
        model=ProfileModel
        # fields = '__all__'
        fields=['ProfileImage','gender','marital_status','city','address','birthday',
        'intrested_job',]          
    
    def __init__(self, *args, **kwargs):
    
        super(ResumeEditForm, self).__init__(*args, **kwargs)
        nonRequriedFields=['ProfileImage','gender','marital_status','city','address','birthday',
        'intrested_job',]   

        # datefields=['birthday',]
   
        self.fields["birthday"] = forms.DateField(widget=forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES))

        for key in nonRequriedFields:
            self.fields[key].required = False
        
        


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}),label="رمز عبور قبلی")
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}),label="رمز عبور جدید")
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}),label="تکرار رمز عبور جدید")
    
    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']



class skillForm(forms.ModelForm):
    class Meta:
        model = skillsModel
        fields = ['skillname',
            'levelofskill']
            

# skillFormSet=inlineformset_factory(ProfileModel, skillsModel, fields=('skillname','levelofskill' ),
#     extra=1,
#     widgets={'skillname': forms.TextInput(attrs={
#              'class': 'formedit ',
#              'placeholder': ''
#              }),
#             'levelofskill': forms.Select(attrs={
#                 'class': 'formedit',
#                 'placeholder': ''
#             })
#              })
skillFormSetinstance=inlineformset_factory(ProfileModel, skillsModel, fields=('skillname','levelofskill' ),
    extra=0,
    widgets={'skillname': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'levelofskill': forms.Select(attrs={
                'class': 'formedit',
                'placeholder': ''
            })
             },
             )
skillFormSet = modelformset_factory(
    skillsModel,
    fields=('skillname','levelofskill' ),
    extra=1,
    widgets={'skillname': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'levelofskill': forms.Select(attrs={
                'class': 'formedit',
                'placeholder': ''
            })
             },
    error_messages={
    'skillname': {
        'required': 'some custom required message',
    },
    'levelofskill': {
        'required': 'some required message',
    },
 },
 
)

aducationFormSet = modelformset_factory(
    aducationModel,
    fields=('degree_level','major','university','gpa','from_year','to_year' ),
    extra=1,
    # widgets=forms.CharField(attrs={'class':'formedit'})
    widgets={'degree_level': forms.Select(attrs={
             'class': 'formedit',
             
             }),
            'major': forms.TextInput(attrs={
                'class': 'formedit',
                
            }),
            'university': forms.TextInput(attrs={
                'class': 'formedit',
                
            }),
            'gpa': forms.TextInput(attrs={
                'class': 'formedit',
                
            }),
            'from_year': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            'to_year': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
             }
)

aducationFormSetinstance=inlineformset_factory(ProfileModel, aducationModel, 
    fields=('degree_level','major','university','gpa','from_year','to_year' ),
    extra=0,
    widgets={'degree_level': forms.Select(attrs={
             'class': 'formedit',
             
             }),
            'major': forms.TextInput(attrs={
                'class': 'formedit',
                
            }),
            'university': forms.TextInput(attrs={
                'class': 'formedit',
                
            }),
            'gpa': forms.TextInput(attrs={
                'class': 'formedit',
                
            }),
            'from_year': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            'to_year': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
             }
    )


workexperienceFormSetinstance=inlineformset_factory(ProfileModel, workexperienceModel, fields=('job_title','company_name','start_time','end_time' ),
    extra=0,
    widgets={'job_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'company_name': forms.TextInput(attrs={
                'class': 'formedit',
                'placeholder': ''
            }),
            
            'start_time': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            'end_time': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
             })
workexperienceFormSet = modelformset_factory(
    workexperienceModel,
    fields=('job_title','company_name','start_time','end_time' ),
    extra=1,
    widgets={'job_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'company_name': forms.TextInput(attrs={
                'class': 'formedit',
                'placeholder': ''
            }),
            'start_time': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            'end_time': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
             }
)

coursesFormSetinstance=inlineformset_factory(ProfileModel, coursesModel, fields=('coursesname','institute', ),
    extra=0,
    widgets={'coursesname': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'institute': forms.TextInput(attrs={
                'class': 'formedit',
                'placeholder': ''
            }),
            
             })
coursesFormSet = modelformset_factory(
    coursesModel,
    fields=('coursesname','institute', ),
    extra=1,
    widgets={'coursesname': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'institute': forms.TextInput(attrs={
                'class': 'formedit',
                'placeholder': ''
            }),
           
             }
)



awardFormSetinstance=inlineformset_factory(ProfileModel, awardsModel, fields=('award_title','dateofaward', ),
    extra=0,
    widgets={'award_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'dateofaward': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            
             })
awardFormSet = modelformset_factory(
    awardsModel,
    fields=('award_title','dateofaward', ),
    extra=1,
    widgets={'award_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'dateofaward': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            
             }
)



projectsFormSetinstance=inlineformset_factory(ProfileModel, projectsModel, fields=('project_title','dateofproject', ),
    extra=0,
    widgets={'project_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'dateofproject': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            
             })
projectsFormSet = modelformset_factory(
    projectsModel,
    fields=('project_title','dateofproject', ),
    extra=1,
    widgets={'project_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'dateofproject': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            
             }
)


articleFormSetinstance=inlineformset_factory(ProfileModel, articlesModel, fields=('article_title','dateofarticle', ),
    extra=0,
    widgets={'article_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'dateofarticle': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            
             })
articleFormSet = modelformset_factory(
    articlesModel,
    fields=('article_title','dateofarticle', ),
    extra=1,
    widgets={'article_title': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'dateofarticle': forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'], years=YEAR_CHOICES, months=MONTH_CHOICES),
            
             }
)



languagesFormSetinstance=inlineformset_factory(ProfileModel, languagesModel, fields=('language','leveloflanguage', ),
    extra=0,
    widgets={'language': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'leveloflanguage': forms.Select(attrs={
                'class': 'formedit',
                'placeholder': ''
            }),
            
             })
languagesFormSet = modelformset_factory(
    languagesModel,
    fields=('language','leveloflanguage', ),
    extra=1,
    widgets={'language': forms.TextInput(attrs={
             'class': 'formedit ',
             'placeholder': ''
             }),
            'leveloflanguage': forms.Select(attrs={
                'class': 'formedit',
                'placeholder': ''
            }),
            
             }
)