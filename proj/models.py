from django.db import models
from datetime import date,datetime
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class Record(models.Model):
    user = models.EmailField(max_length=254)
    doctor = models.EmailField(max_length=254)
    rdate = models.DateField(default=date.today)
    adate=models.DateTimeField(null=True)
    status=models.IntegerField(default=0)
    # presarray=ArrayField(models.CharField(max_length=100),blank=True,null=True)
    prescription=models.CharField(max_length=100,null=True)
    bill=models.CharField(max_length=100,null=True)
    feedst=models.IntegerField(default=0)

class Orders(models.Model):
    tid=models.IntegerField(default=0)
    user = models.EmailField(max_length=254)
    pharma = models.EmailField(max_length=254)
    prescription=models.CharField(max_length=100,null=True)
    bill=models.CharField(max_length=100,null=True)
    rdate = models.DateField(default=date.today)
    adate=models.DateTimeField(null=True)
    status=models.IntegerField(default=0)

class Messages(models.Model):
    sender = models.EmailField(max_length=254)
    receiver = models.EmailField(max_length=254)
    message = models.CharField(max_length=254)
    time = models.DateTimeField(default=timezone.now)
    read=models.IntegerField(default=0)


class Prescription(models.Model):
    tid=models.IntegerField(default=0)
    mediname= models.CharField(max_length=254)
    meditype=models.CharField(max_length=254)
    quantity=models.IntegerField(default=0)
    meal=models.CharField(max_length=254)
    time=ArrayField(models.CharField(max_length=100),blank=True,null=True)
    cost=models.IntegerField(default=0)

class Feedback(models.Model):
    tid=models.IntegerField(default=0)
    user = models.EmailField(max_length=254)
    doctor = models.EmailField(max_length=254)
    feedback=models.CharField(max_length=100,null=True)
    rating=models.IntegerField(default=0)


