from django.db import models
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Registration(models.Model):
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_OTHERS = "O"
    CATALOGUE_PRESENT='p'
    CATALOGUE_EX='E'
    CATALOGUE_OTHERS='O'
    CATALOGUE_CHOICES=[(CATALOGUE_PRESENT,'PRESENT'),(CATALOGUE_EX,'EX'),(CATALOGUE_OTHERS,'OTHERS')]
    GENDER_CHOICES = [(GENDER_MALE, 'MALE'), (GENDER_FEMALE, 'FEMALE'),(GENDER_OTHERS,'OTHERS')]
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    password1 = models.CharField(max_length=30,default='')
    password2 = models.CharField(max_length=30)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    age=models.IntegerField(default=19)
    phone_number=PhoneNumberField(blank=True)
    catalogue=models.CharField(max_length=50,choices=CATALOGUE_CHOICES,default=CATALOGUE_PRESENT)

    def __str__(self):
        return self.name

class Login(models.Model):
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
