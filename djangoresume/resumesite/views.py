from multiprocessing import context
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from .models import aboutmeModel
from .serializers import aboutmeModelSerializers
from .models import aboutmeModel,skillsModel,aducationModel,workexperience,coursesModel
# Create your views here.
def home(request):
    aboutMeModel=aboutmeModel.objects.all()
    Workexperience=workexperience.objects.all()
    AducationModel=aducationModel.objects.all()
    SkillsModel=skillsModel.objects.all()
    CoursesModel=coursesModel.objects.all()
    context={
        'aboutMeModel':aboutMeModel,
        'Workexperience':Workexperience,
        'AducationModel':AducationModel,
        'SkillsModel':SkillsModel,
        'CoursesModel':CoursesModel
    }
    return render(request,'home.html',context)


def fahome(request):
    aboutMeModel=aboutmeModel.objects.all()
    Workexperience=workexperience.objects.all()
    AducationModel=aducationModel.objects.all()
    SkillsModel=skillsModel.objects.all()
    CoursesModel=coursesModel.objects.all()
    context={
        'aboutMeModel':aboutMeModel,
        'Workexperience':Workexperience,
        'AducationModel':AducationModel,
        'SkillsModel':SkillsModel,
        'CoursesModel':CoursesModel
    }
    return render(request,'fahome.html',context)


class aboutmeview(viewsets.ModelViewSet):
    queryset=aboutmeModel.objects.all()
    serializer_class=aboutmeModelSerializers
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
