
from urllib import request
from django.shortcuts import render,redirect,HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')



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
        
        myuser=User(username=name,email=email,password=password1,gender=gender,age=age,phone_number=phone_number,catalogue=catalogue)
        myuser.save()
        return redirect('login')
    return render(request,'app/register.html')



def loginPage(request):
    if request.method=='POST':
        email =request.POST['email']
        password=request.POST['password']

        user=User.objects.get(email=email)
        print(user.email)
        print(user.password)
        if (user.email== email and user.password == password):
               return render(request,'app/AllCards.html')

        else:
            redirect('home')

      

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
    
        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']
            name1=request.POST['name1']
            id1=request.POST['id1']
            name2=request.POST['name2']
            id2=request.POST['id2']
            name3=request.POST['name3']
            id3=request.POST['id3']
            myuser=Badminton(teamname=teamname,dept=dept,captainname=captainname,cid=cid,name1=name1,id1=id1,name2=name2,id2=id2,name3=name3,id3=id3)
            myuser.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/badminton_rule.html')

def chess_rule(request):
     return render(request,'app/chess_rule.html')


def cricket_rule(request):
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


def cricket_form(request):
     return render(request,'app/cricket_form.html')

def football_form(request):
     return render(request,'app/football_form.html')

def volleyball_form(request):
     return render(request,'app/volleyball_form.html')

def kabaddi_form(request):
     return render(request,'app/kabaddi_form.html')

def video_form(request):
     return render(request,'app/video_form.html')

def pc3_form(request):
     return render(request,'app/pc3_form.html')

def badminton_form(request):
     return render(request,'app/badminton_form.html')


def chess_form(request):
     return render(request,'app/chess_form.html')

def highjump_form(request):
     return render(request,'app/highjump_form.html')

def pc1_form(request):
     return render(request,'app/pc1_form.html')

def math_form(request):
     return render(request,'app/math_form.html')

def ict_form(request):
     return render(request,'app/ict_form.html')

def rubkis_form(request):
     return render(request,'app/rubiks_form.html')

def table_form(request):
     return render(request,'app/table_form.html')
def sprint_form(request):
     return render(request,'app/sprint_form.html')





