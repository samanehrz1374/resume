from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import aboutmeModel

class aboutmeModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=aboutmeModel
        fields=('id','Name','LastName','Email')
        