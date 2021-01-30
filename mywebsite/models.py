from django.db import models
from django.utils import timezone

now = timezone.now()

# Create your models here.
class signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()

    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    block=models.CharField(max_length=20)
    house=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.fname
#create Complain Model

class complain(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    block=models.CharField(max_length=20)
    house=models.CharField(max_length=20)
    complaintype=models.CharField(max_length=20)
    discription=models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname

   #for contact form

class contact(models.Model):
    fname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    Buy=models.CharField(max_length=20)  
    subject=models.CharField(max_length=20)   

    def __str__(self):
        return self.fname  
