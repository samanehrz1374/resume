from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import aboutmeModel

class aboutmeModelSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=aboutmeModel
        fields=('id','url','Name','LastName','Email')
