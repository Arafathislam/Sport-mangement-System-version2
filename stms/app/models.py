from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(models.Model):
 

    CATALOGUE_CHOICES=[('Present','Present'),('Ex','Ex'),('Others','Others')]
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'),('Others','Others')]
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,unique=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    age=models.IntegerField(default=19)
    phone_number=PhoneNumberField(blank=True)
    catalogue=models.CharField(max_length=50,choices=CATALOGUE_CHOICES)



    def __str__(self):
        return self.email


class Badminton(models.Model):
 

    DEPT_CHOICES=[('CSE','CSE'),
                  ('Pharmacy','Pharmacy'),
                  ('BBA','BBA'),
                  ('Law','Law'),
                  ('Fashion Design','Fashion Design'),
                  ('English','English')
                  ]
    
    teamname=models.CharField(max_length=20)
    dept=models.CharField(max_length=20,choices=DEPT_CHOICES)
    captainname=models.CharField(max_length=20)
    cid=models.IntegerField()
    name1=models.CharField(max_length=20)
    id1=models.IntegerField()
    name2=models.CharField(max_length=20)
    id2=models.IntegerField()
    name3=models.CharField(max_length=20)
    id3=models.IntegerField()




    def __str__(self):
        return self.teamname



