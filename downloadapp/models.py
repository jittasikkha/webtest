import email
from unicodedata import name
from venv import create
from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=500)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    room = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.room


class File(models.Model):
    upload = models.FileField(upload_to = 'file')
    image = models.ImageField(upload_to = 'img')
    name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey('Subject' , on_delete=models.SET_NULL,blank=True,null=True)
    room = models.ForeignKey('Room' , on_delete=models.SET_NULL,blank=True , null=True )
    approved = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)



    def __str__(self) -> str:
        return self.name


class Province(models.Model):
    province = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.province

class Role(models.Model):
    role = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.role

class Client(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    role = models.ForeignKey('Role' , on_delete=models.CASCADE , null=True , blank=True)
    province = models.ForeignKey('Province' , on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)
    create = models.DateTimeField(auto_now_add=True)
    


    def __str__(self) -> str:
        return self.email





