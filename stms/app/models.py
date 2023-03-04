from django.db import models
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser):
 



    CATALOGUE_CHOICES=[('P','Present'),('E','Ex'),('O','Others')]
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'),('O','Others')]

    username=None

    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    age=models.IntegerField(default=19)
    phone_number=PhoneNumberField(blank=True)
    catalogue=models.CharField(max_length=50,choices=CATALOGUE_CHOICES)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email

