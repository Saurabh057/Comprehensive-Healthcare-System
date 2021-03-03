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


class Orders(models.Model):
    user = models.EmailField(max_length=254)
    pharma = models.EmailField(max_length=254)
    medicines=models.CharField(max_length=254)
    rdate = models.DateField(default=date.today)
    adate=models.DateTimeField(null=True)
    status=models.IntegerField(default=0)

class Messages(models.Model):
    sender = models.EmailField(max_length=254)
    receiver = models.EmailField(max_length=254)
    message = models.CharField(max_length=254)
    time = models.DateTimeField(default=timezone.now)
    read=models.IntegerField(default=0)
