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
from accounts.forms import (ProfileRegisterForm,ProfileEditForm,UserEditForm,ResumeEditForm,PasswordChangingForm,
                            skillFormSet,aducationFormSet,skillFormSetinstance,
                            aducationFormSetinstance,workexperienceFormSetinstance,
                            workexperienceFormSet,coursesFormSet,coursesFormSetinstance,
                            awardFormSet,awardFormSetinstance,projectsFormSet,
                            projectsFormSetinstance,languagesFormSet,languagesFormSetinstance,
                            articleFormSetinstance,articleFormSet)
from django.contrib.auth.models import User
from accounts.models import ProfileModel,skillsModel,aducationModel,articlesModel,awardsModel,workexperienceModel,projectsModel,languagesModel,coursesModel
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# from django.core.mail import send_mail,BadHeaderError
# from django.contrib.auth.forms import PasswordResetForm
# from django.template.loader import render_to_string
# from django.db.models.query_utils import Q
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode





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
            messages.success(request, 'ثبت نام شما انجام شد. برای ورود کلیک کنید.')
            return render(request, 'accounts/registrationsuccess.html', {'form': profileRegisterForm})
            
            
            
            # return HttpResponseRedirect(reverse(accounts.views.loginpanelview))

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
    skill=skillsModel.objects.filter(skills_id=resumeprofile)
    aducation=aducationModel.objects.filter(aducations_id=resumeprofile)
    award=awardsModel.objects.filter(awards_id=resumeprofile)
    article=articlesModel.objects.filter(articles_id=resumeprofile)
    course=coursesModel.objects.filter(courses_id=resumeprofile)
    language=languagesModel.objects.filter(languages_id=resumeprofile)
    project=projectsModel.objects.filter(projects_id=resumeprofile)
    workexperience=workexperienceModel.objects.filter(jobs_id=resumeprofile)

    
    context={
        "resumeprofile":resumeprofile,
        "skill":skill,
        "aducation":aducation,
        "award":award,
        "article":article,
        "course":course,       
        "language":language,
        "project":project,
        "workexperience":workexperience,

        
    }
    return render(request,"accounts/resumeprofile.html",context)

@login_required
def ResumeEditView(request):
    profile = request.user.profile
    skillprofile=skillsModel.objects.filter(skills_id=profile)
    aducationprofile=aducationModel.objects.filter(aducations_id=profile)
    skillformsetinstance = skillFormSetinstance(skillsModel.objects.all())
    aducationformSetinstance=aducationFormSetinstance(aducationModel.objects.all())
    skillformset = skillFormSet(queryset=skillsModel.objects.none())
    aducationformSet=aducationFormSet(queryset=aducationModel.objects.none())
    workexperienceformSetinstance=workexperienceFormSetinstance(aducationModel.objects.all())
    workexperienceformSet=workexperienceFormSet(queryset=workexperienceModel.objects.none())
    workexperience=workexperienceModel.objects.filter(jobs_id=profile)
    coursesformSet = coursesFormSet(queryset=coursesModel.objects.none())
    coursesformSetinstance = coursesFormSetinstance(coursesModel.objects.all())
    course=coursesModel.objects.filter(courses_id=profile)

    awardformSet = awardFormSet(queryset=awardsModel.objects.none())
    awardformSetinstance = awardFormSetinstance(awardsModel.objects.all())
    award=awardsModel.objects.filter(awards_id=profile)

    projectsformSet = projectsFormSet(queryset=projectsModel.objects.none())
    projectsformSetinstance = projectsFormSetinstance(projectsModel.objects.all())
    project=projectsModel.objects.filter(projects_id=profile)

    articleformSet = articleFormSet(queryset=articlesModel.objects.none())
    articleformSetinstance = articleFormSetinstance(articlesModel.objects.all())
    article=articlesModel.objects.filter(articles_id=profile)

    languagesformSet = languagesFormSet(queryset=languagesModel.objects.none())
    languagesformSetinstance = languagesFormSetinstance(languagesModel.objects.all())
    language=languagesModel.objects.filter(languages_id=profile)
    

    if request.method == 'POST':
        if 'skilladd' in request.POST:
            profile = request.user.profile
            skillformset = skillFormSet(request.POST)
            

            if skillformset.is_valid():
                    for skillform in skillformset:
                        
                        if skillform.cleaned_data != {}:
                            skill = skillform.save(commit=False)
                            skill.skills = profile 
                            skill.save()
        

        if 'skilledit' in request.POST:
            skillformsetinstance = skillFormSetinstance(request.POST,instance=profile)
            if skillformsetinstance.is_valid() :
                skillformsetinstance.save()
        if 'educationadd' in request.POST:
            aducationformSet=aducationFormSet(request.POST)
            if aducationformSet.is_valid():
                for aducationform in aducationformSet:
                    if aducationform.cleaned_data != {}:
                        aducation = aducationform.save(commit=False)
                        aducation.aducations = profile 
                        aducation.save()
        if 'aducationedit' in request.POST:
            aducationformSetinstance = aducationFormSetinstance(request.POST,instance=profile)
            if aducationformSetinstance.is_valid() :
                aducationformSetinstance.save()
        if 'workexperienceadd' in request.POST:
            workexperienceformSet = workexperienceFormSet(request.POST)
           
            if workexperienceformSet.is_valid():
                for workexperienceform in workexperienceformSet:
                    if workexperienceform.cleaned_data != {}:
                        workexperience = workexperienceform.save(commit=False)
                        workexperience.jobs = profile 
                        workexperience.save()
            
        if 'workexperienceedit' in request.POST:
            workexperienceformSetinstance = workexperienceFormSetinstance(request.POST,instance=profile)
            if workexperienceformSetinstance.is_valid() :
                workexperienceformSetinstance.save()

        if 'courcesadd' in request.POST:
            coursesformSet = coursesFormSet(request.POST)
            if coursesformSet.is_valid():
                for coursesform in coursesformSet:
                    if coursesform.cleaned_data != {}:
                        courses = coursesform.save(commit=False)
                        courses.courses = profile 
                        courses.save()
            
        if 'courcessedit' in request.POST:
            coursesformSetinstance = coursesFormSetinstance(request.POST,instance=profile)
            if coursesformSetinstance.is_valid() :
                coursesformSetinstance.save()
        
        if 'awardsadd' in request.POST:
            awardformSet = awardFormSet(request.POST)
            if awardformSet.is_valid():
                for awardform in awardformSet:
                    if awardform.cleaned_data != {}:
                        award = awardform.save(commit=False)
                        award.awards = profile 
                        award.save()
            
            
        if 'awardsedit' in request.POST:
            awardformSetinstance = awardFormSetinstance(request.POST,instance=profile)
            if awardformSetinstance.is_valid() :
                awardformSetinstance.save()


        if 'articleadd' in request.POST:
            articleformSet = articleFormSet(request.POST)
            if articleformSet.is_valid():
                for articleform in articleformSet:
                    if articleform.cleaned_data != {}:
                        article = articleform.save(commit=False)
                        article.articles = profile 
                        article.save()
            
            
        if 'articleedit' in request.POST:
            articleformSetinstance = articleFormSetinstance(request.POST,instance=profile)
            if articleformSetinstance.is_valid() :
                articleformSetinstance.save()

        if 'projectsadd' in request.POST:
            projectsformSet = projectsFormSet(request.POST)
            if projectsformSet.is_valid():
                for projectsform in projectsformSet:
                    if projectsform.cleaned_data != {}:
                        project = projectsform.save(commit=False)
                        project.projects = profile 
                        project.save()
            
            
        if 'projectsedit' in request.POST:
            projectsformSetinstance = projectsFormSetinstance(request.POST,instance=profile)
            if projectsformSetinstance.is_valid() :
                projectsformSetinstance.save()

        if 'languagesadd' in request.POST:
            languagesformSet = languagesFormSet(request.POST)
            if languagesformSet.is_valid():
                for languagesform in languagesformSet:
                    if languagesform.cleaned_data != {}:
                        language = languagesform.save(commit=False)
                        language.languages = profile 
                        language.save()
            
            
        if 'languagesedit' in request.POST:
            languagesformSetinstance = languagesFormSetinstance(request.POST,instance=profile)
            if languagesformSetinstance.is_valid() :
                languagesformSetinstance.save()

        if 'profileedit' in request.POST:
           resumeeditform=ResumeEditForm(request.POST,request.FILES,instance=request.user.profile)
           usereditform=UserEditForm(request.POST,instance=request.user)
           if resumeeditform.is_valid() and usereditform.is_valid():
               resumeeditform.save()
               usereditform.save()
        return HttpResponseRedirect(reverse(accounts.views.ResumeEditView))

    else:
        resumeeditform=ResumeEditForm(instance=request.user.profile)
        usereditform=UserEditForm(instance=request.user)
        skillformsetinstance = skillFormSetinstance(instance=profile)
        aducationformSetinstance=aducationFormSetinstance(instance=profile)
        workexperienceformSetinstance=workexperienceFormSetinstance(instance=profile)
        coursesformSetinstance = coursesFormSetinstance(instance=profile)
        awardformSetinstance = awardFormSetinstance(instance=profile)
        projectsformSetinstance = projectsFormSetinstance(instance=profile)
        articleformSetinstance = articleFormSetinstance(instance=profile)
        languagesformSetinstance = languagesFormSetinstance(instance=profile)


    context={
        "skill":skillprofile,
        "resumeeditform":resumeeditform,
        "usereditform":usereditform,
        "ProfileImage":request.user.profile.ProfileImage,
        "skillformset":skillformset,
        "aducationformSet":aducationformSet,
        "author":profile,
        "skillformsetinstance":skillformsetinstance,
        "aducationprofile":aducationprofile,
        "aducationformSetinstance":aducationformSetinstance,
        "resumeprofile":profile,
        "workexperienceformSetinstance":workexperienceformSetinstance,
        "workexperienceformSet":workexperienceformSet,
        "workexperience":workexperience,
        "coursesformSetinstance":coursesformSetinstance,
        "course":course,
        "coursesformSet":coursesformSet,
        "awardformSetinstance":awardformSetinstance,
        "awardformSet":awardformSet,
        "award":award,
        "projectsformSetinstance":projectsformSetinstance,
        "projectsformSet":projectsformSet,
        "project":project,
        "articleformSetinstance":articleformSetinstance,
        "articleformSet":articleformSet,
        "article":article,
        "languagesformSetinstance":languagesformSetinstance,
        "languagesformSet":languagesformSet,
        "language":language



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

