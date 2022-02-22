from email.policy import default
from django.urls import reverse, reverse_lazy
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
import accounts
from django.contrib.auth.decorators import login_required
from django.conf import settings
from resumesite import views
import resumesite
from accounts.forms import ProfileRegisterForm,ProfileEditForm,UserEditForm,ResumeEditForm,PasswordChangingForm
from django.contrib.auth.models import User
from accounts.models import ProfileModel
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode





# Create your views here.
def loginVeiw(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            

        else:
            context={
                "username":username,
                "errormassage":"کاربری با این مشخصات وجود ندارد"

            }
            return render(request,"accounts/login.html",context)
    else:
        return render(request,"accounts/login.html",{})

@login_required
def loginpanelview(request):
    profile=request.user.profile
    context={
        "profile":profile
    }
    return render(request,"accounts/loginpanelFa.html",context)

def logoutVeiw(request):
    logout(request)
    return HttpResponseRedirect(reverse(loginVeiw))

def profileRegisterView(request):
    profileRegisterForm=ProfileRegisterForm()
    if request.method=="POST":
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                email=profileRegisterForm.cleaned_data['email'],
                                password=profileRegisterForm.cleaned_data['password'],
                                first_name=profileRegisterForm.cleaned_data['first_name'],
                                last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel=ProfileModel(user=user,
                                       ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],
                                       gender=profileRegisterForm.cleaned_data['gender'])

            profileModel.save()
            # login(request,user)
            
            return HttpResponseRedirect(reverse(accounts.views.loginpanelview))

    context={
        "formData":profileRegisterForm
    }
    return render(request,"accounts/profileregister.html",context)
@login_required
def profileView(request):
    profile=request.user.profile
    context={
        "profile":profile
    }
    return render(request,"accounts/profile.html",context)


def ProfileEditView(request):
    if request.method=="POST":
        profileeditform=ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)
        usereditform=UserEditForm(request.POST,instance=request.user)
        if profileeditform.is_valid() and usereditform.is_valid():
            profileeditform.save()
            usereditform.save()
            return HttpResponseRedirect(reverse(accounts.views.profileView))

    else:
        profileeditform=ProfileEditForm(instance=request.user.profile)
        usereditform=UserEditForm(instance=request.user)

    context={
        "profileeditform":profileeditform,
        "usereditform":usereditform,
        "ProfileImage":request.user.profile.ProfileImage,
    }
    return render(request,"accounts/profileEdit.html",context)



@login_required
def resumeprofileview(request):
    resumeprofile=request.user.profile
    
    context={
        "resumeprofile":resumeprofile
        
    }
    return render(request,"accounts/resumeprofile.html",context)

@login_required
def ResumeEditView(request):
    if request.method=="POST":
        resumeeditform=ResumeEditForm(request.POST,request.FILES,instance=request.user.profile)
        usereditform=UserEditForm(request.POST,instance=request.user)
        if resumeeditform.is_valid() and usereditform.is_valid():
            resumeeditform.save()
            usereditform.save()
            return HttpResponseRedirect(reverse(accounts.views.resumeprofileview))

    else:
        resumeeditform=ResumeEditForm(instance=request.user.profile)
        usereditform=UserEditForm(instance=request.user)

    context={
        "resumeeditform":resumeeditform,
        "usereditform":usereditform,
        "ProfileImage":request.user.profile.ProfileImage,
    }
    return render(request,"accounts/resumeEdit.html",context)


def loginen(request):
    return render(request,"accounts/loginpanelEn.html",{})


def passwordchangeview(request):
    if request.method == 'POST':
        form = PasswordChangingForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse(accounts.views.loginpanelview))
    else:
        form = PasswordChangingForm(request.user)
    return render(request, 'accounts/passwordchange.html', {'form': form})


# def passwordreset(request):
#     if request.method == 'POST':
#         password_form=PasswordResetForm(request.POST)
#         if password_form.is_valid():
#             data = password_form.cleaned_data['email']
#             user_email = User.objects.filter(Q(email=data))
#             if user_email.exists():
#                 for user in user_email:
#                     subject = 'Password Resquest'
#                     email_template_name='accounts/massage.txt'
#                     parameters={
#                         'email': user.email,
#                         'domain':'127.0.0.1:8000',
#                         'site_name':'PostScribers',
#                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                         'token':default_token_generator.make_token(user),
#                         'protocol':'http',
#                     }
#                     email = render_to_string(email_template_name,parameters)
#                     try:
#                         send_mail(subject,email,'',[user.email],fail_silently=False)
#                     except:
#                         return HttpResponse('Invalid Header')
#                     return  redirect('password_reset_done')  
#     else:       


#         password_form=PasswordResetForm()
#     context={
#         'password_form':password_form
#     }
#     return render(request,'accounts/password_reset.html', context)