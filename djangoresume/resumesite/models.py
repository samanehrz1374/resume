from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class aboutmeModel(models.Model):
    Name=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.Name