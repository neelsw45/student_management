from django.db import models

# Create your models here.
class Addmission(models.Model):
    sname=models.CharField(max_length=30)
    semail=models.EmailField(default='student@123gmail.com')
    sphoneno=models.IntegerField()
    senrollno=models.IntegerField()
    sadddate=models.DateField()
    paid_fees = models.BooleanField(default=False)
    # sfees=models.BooleanField(default=False)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(default='user@gmail.com')
    phno=models.IntegerField()
    desc=models.TextField()
