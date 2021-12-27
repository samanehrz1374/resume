from django.db import models

# Create your models here.
class aboutmeModel(models.Model):
    Name=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()

    def __str__(self):
        return self.Name