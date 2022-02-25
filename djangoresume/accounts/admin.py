from django.contrib import admin
from .models import ProfileModel, aducationModel,skillsModel,coursesModel,languagesModel,projectsModel,articlesModel,awardsModel, workexperienceModel,aducationModel,workexperienceModel



class aducation(admin.TabularInline):
    model = aducationModel

class workexperience(admin.TabularInline):
    model = workexperienceModel

class skill(admin.TabularInline):
    model = skillsModel

class course(admin.TabularInline):
    model = coursesModel

class language(admin.TabularInline):
    model = languagesModel

class project(admin.TabularInline):
    model = projectsModel  

class article(admin.TabularInline):
    model = articlesModel  

class award(admin.TabularInline):
    model = awardsModel  

class AuthorAdmin(admin.ModelAdmin):
    inlines = [skill,course,language,project,article,award,aducation,workexperience]


admin.site.register(ProfileModel, AuthorAdmin)

# Register your models here.
#admin.site.register(ProfileModel)
