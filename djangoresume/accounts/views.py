from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
import accounts
from django.contrib.auth.decorators import login_required
from django.conf import settings
from resumesite import views
import resumesite
from accounts.forms import ProfileRegisterForm
from django.contrib.auth.models import User
from accounts.models import ProfileModel
from django.contrib import messages


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
    return render(request,"accounts/loginpanelFa.html",{})

def logoutVeiw(request):
    logout(request)
    return render(request,"accounts/login.html",{})

def profileRegisterView(request):
    
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
                                       profileimage=profileRegisterForm.cleaned_data['profileimage'],
                                       gender=profileRegisterForm.cleaned_data['gender'])
                                        # birthday=profileRegisterForm.cleaned_data['birthday'])

            profileModel.save()

            return HttpResponse('o')
    else:
        profileRegisterForm=ProfileRegisterForm()

  
    context={
        "formData":profileRegisterForm
    }
    return render(request,"accounts/profileregister.html",context)




    
