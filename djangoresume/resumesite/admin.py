from django.contrib import admin
from .models import aboutmeModel
from .models import aducationModel,workexperience,languagesModel,skillsModel,coursesModel,awardsModel,projectsModel,articlesModel
# Register your models here.
admin.site.register(aboutmeModel)
admin.site.register(aducationModel)
admin.site.register(workexperience)
admin.site.register(languagesModel)
admin.site.register(skillsModel)
admin.site.register(coursesModel)
admin.site.register(awardsModel)
admin.site.register(projectsModel)
admin.site.register(articlesModel)
