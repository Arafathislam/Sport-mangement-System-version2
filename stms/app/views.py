
from urllib import request
from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

from app.models import Registration
# Create your views here.

def home(request):
    return render(request,'main.html')


def allcards(request):
    return render(request,'app/AllCards.html')



def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        gender=request.POST['gender']
        age=request.POST['age']
        phone_number=request.POST['phone_number']
        catalogue=request.POST['catalogue']
        myuser=Registration(name=name,email=email,password1=password1, password2=password2,gender=gender,age=age,phone_number=phone_number,catalogue=catalogue)
        myuser.save()
    return render(request,'app/main.html')



def loginPage(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            return render(request,'app/done.html')
        else:
            return redirect('/')







