from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import aboutmeModel
from .serializers import aboutmeModelSerializers
# Create your views here.
def home(request):
    return render(request,'home.html',{})


def fahome(request):
    return render(request,'fahome.html',{})


class aboutmeview(viewsets.ModelViewSet):
    queryset=aboutmeModel.objects.all()
    serializer_class=aboutmeModelSerializers