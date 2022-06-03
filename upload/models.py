from urllib import response
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Area(models.Model):
    area=models.CharField(max_length=50)
    def __str__(self):
        return self.area

class File(models.Model):
    name=models.CharField(max_length=10)
    file=models.FileField(upload_to="files")
    area=models.ManyToManyField(Area)
    def __str__(self):
        return self.name

class Summary(models.Model):
    file=models.OneToOneField(File, on_delete= models.CASCADE)
    summary=models.TextField()
    def __str__(self):
        return self.file.name