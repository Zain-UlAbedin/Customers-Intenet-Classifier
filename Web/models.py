from django.db import models

# Create your models here.


class User(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=200)


class File(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    File_Name = models.CharField(max_length=500)
    File_Path = models.FileField(upload_to='static/Files')
    File_Size = models.FloatField()
    Lable = models.BooleanField()


class File_data(models.Model):
    File_Name = models.CharField(max_length=500)
    Complain = models.IntegerField()
    Recommend = models.IntegerField()
    Query = models.IntegerField()
    Appreciation = models.IntegerField()
    Others = models.IntegerField()
