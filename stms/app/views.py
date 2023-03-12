
from urllib import request
from django.shortcuts import render,redirect,HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    return render(request,'app/home.html')



def register(request):
    # if request.method == 'POST':
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     password1=request.POST['password1']
    #     password2=request.POST['password2']
    #     gender=request.POST['gender']
    #     age=request.POST['age']
    #     phone_number=request.POST['phone_number']
    #     catalogue=request.POST['catalogue']
        
    #     myuser=User.crea(fullname=name,email=email,password=password1,gender=gender,age=age,phone_number=phone_number,catalogue=catalogue)
    #     myuser.save()
    return render(request,'app/register.html')



def loginPage(request):
    # if request.method=='POST':
    #     email = request.POST.get('email')
    #     password=request.POST.get('password')

    #     m=User.objects.get(email=email)
        
    #     # user=authenticate(request,email=email,password=password)


    #     # if user is not None:
    #     #     login(request,user)
    #     #     return render(request,'app/done.html')
    #     # else:
    #     #  return render(request,'main.html')

    #     if(m.email==email and m.password==password):
            return render(request,'app/login.html')

def tournament(request):
    return render(request,'app/tournament.html')



def news(request):
    return render(request,'app/news.html')

def contact(request):
    return render(request,'app/contact.html')


def about(request):
    return render(request,'app/about.html')



def allcards(request):
    return render(request,'app/AllCards.html')



def badminton_rule(request):
     return render(request,'app/badminton_rule.html')

def chess_rule(request):
     return render(request,'app/chess_rule.html')


def criket_rule(request):
     return render(request,'app/cricket.html')

def football_rule(request):
     return render(request,'app/football.html')

def highjump_rule(request):
     return render(request,'app/highjump.html')

def pc3_rule(request):
     return render(request,'app/pc3.html')

def kabaddi_rule(request):
     return render(request,'app/kabaddi.html')

def pc1_rule(request):
     a=pc1_rule
     context={'a':a}
     return render(request,'app/pc1.html',context)

def math_rule(request):
     return render(request,'app/math.html')

def video_rule(request):
     return render(request,'app/video.html')

def ict_rule(request):
     return render(request,'app/ict.html')

def rubiks_rule(request):
     return render(request,'app/rubiks.html')

def table_rule(request):
     return render(request,'app/table.html')

def volleyball_rule(request):
     return render(request,'app/volleyball.html')

def sprint_rule(request):
     return render(request,'app/sprint.html')




