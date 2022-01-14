from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
import accounts
from django.contrib.auth.decorators import login_required
from django.conf import settings
from resumesite import views
import resumesite

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




