from django.db import models
from datetime import date
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class AddtionalDetails(models.Model):
    username = models.EmailField(max_length=254)
    name=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=10)
    bdate=models.DateField(null=True)
    address=models.TextField(max_length=50)
    city=models.CharField(max_length=10)
    pin=models.CharField(max_length=6)
    gender=models.CharField(max_length=10)    
    profession=models.CharField(max_length=10,default="user")
    notifications=ArrayField(models.CharField(max_length=100),blank=True,null=True)


class Record(models.Model):
    user = models.EmailField(max_length=254)
    doctor = models.EmailField(max_length=254)
    rdate = models.DateField(default=date.today)
    adate=models.DateField(null=True)
    status=models.IntegerField(default=0)

