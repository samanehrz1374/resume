from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
import accounts
from django.contrib.auth.decorators import login_required
from django.conf import settings
from resumesite import views
import resumesite
from accounts.forms import ProfileRegisterForm,ProfileEditForm,UserEditForm,ResumeEditForm
from django.contrib.auth.models import User
from accounts.models import ProfileModel




# Create your views here.
def loginVeiw(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # if request.GET.get("chk"):
            #     response=HttpResponse('cokke')
            #     response.set.Cookie('cid',request.Post["username"])
            #     response.set.Cookie('cid2',request.Post["password"])
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
            return render(request,"accounts/login.html",{})

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
