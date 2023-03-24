
from urllib import request
from django.shortcuts import render,redirect,HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import *
import random
# Create your views here.

def home(request):
     team=home_score.objects.all()
     context={'team':team}
     return render(request,'home.html',context)



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
         if request.method == 'POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            mobile=request.POST['mobile']
            msg=request.POST['msg']
  


            user=Contact(fname=fname,
                         lname=lname,
                         email=email,
                         mobile=mobile,   
                         msg=msg,
                         )
            user.save()
            return redirect('home')   


         return render(request,'app/contact.html')


def about(request):
    return render(request,'app/about.html')



def allcards(request):
    return render(request,'app/AllCards.html')



def badminton_rule(request):
        
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

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            coachname=request.POST['coachname']
            dept2=request.POST['dept2']
            captainname=request.POST['captainname']
            cid=request.POST['cid']
            name1=request.POST['name1']
            id1=request.POST['id1']
            name2=request.POST['name2']
            id2=request.POST['id2']
            name3=request.POST['name3']
            id3=request.POST['id3']
            name4=request.POST['name4']
            id4=request.POST['id4']
            name5=request.POST['name5']
            id5=request.POST['id5']
            name6=request.POST['name6']
            id6=request.POST['id6']
            name7=request.POST['name7']
            id7=request.POST['id7']
            name8=request.POST['name8']
            id8=request.POST['id8']
            name9=request.POST['name9']
            id9=request.POST['id9']
            name10=request.POST['name10']
            id10=request.POST['id10']
            name11=request.POST['name11']
            id11=request.POST['id11']
            name12=request.POST['name12']
            id12=request.POST['id12']
            name13=request.POST['name13']
            id13=request.POST['id13']
            user=Cricket(teamname=teamname,
                         dept=dept,
                         coachname=coachname,
                         dept2=dept2,
                         captainname=captainname,
                         cid=cid,
                         name1=name1,
                         id1=id1,
                         name2=name2,
                         id2=id2,
                         name3=name3,
                         id3=id3,
                         name4=name4,
                         id4=id4,
                         name5=name5,
                         id5=id5,
                         name6=name6,
                         id6=id6,                        
                         name7=name7,
                         id7=id7,
                         name8=name8,
                         id8=id8,
                         name9=name9,
                         id9=id9,
                         name10=name10,
                         id10=id10, 
                         name11=name11,
                         id11=id11,
                         name12=name12,
                         id12=id12,
                         name13=name13,
                         id13=id13,  

                         )
            user.save()
            return render(request,'app/AllCards.html')
        return render(request,'app/cricket_form.html')

def football_form(request):
        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            coachname=request.POST['coachname']
            dept2=request.POST['dept2']
            captainname=request.POST['captainname']
            cid=request.POST['cid']
            name1=request.POST['name1']
            id1=request.POST['id1']
            name2=request.POST['name2']
            id2=request.POST['id2']
            name3=request.POST['name3']
            id3=request.POST['id3']
            name4=request.POST['name4']
            id4=request.POST['id4']
            name5=request.POST['name5']
            id5=request.POST['id5']
            name6=request.POST['name6']
            id6=request.POST['id6']
            name7=request.POST['name7']
            id7=request.POST['id7']
            name8=request.POST['name8']
            id8=request.POST['id8']
            name9=request.POST['name9']
            id9=request.POST['id9']
            name10=request.POST['name10']
            id10=request.POST['id10']
            name11=request.POST['name11']
            id11=request.POST['id11']
            name12=request.POST['name12']
            id12=request.POST['id12']
            name13=request.POST['name13']
            id13=request.POST['id13']
            user=Football(teamname=teamname,
                         dept=dept,
                         coachname=coachname,
                         dept2=dept2,
                         captainname=captainname,
                         cid=cid,
                         name1=name1,
                         id1=id1,
                         name2=name2,
                         id2=id2,
                         name3=name3,
                         id3=id3,
                         name4=name4,
                         id4=id4,
                         name5=name5,
                         id5=id5,
                         name6=name6,
                         id6=id6,                        
                         name7=name7,
                         id7=id7,
                         name8=name8,
                         id8=id8,
                         name9=name9,
                         id9=id9,
                         name10=name10,
                         id10=id10, 
                         name11=name11,
                         id11=id11,
                         name12=name12,
                         id12=id12,
                         name13=name13,
                         id13=id13,  

                         )
            user.save()
            return render(request,'app/AllCards.html')
        return render(request,'app/football_form.html')

def volleyball_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            coachname=request.POST['coachname']
            dept2=request.POST['dept2']
            captainname=request.POST['captainname']
            cid=request.POST['cid']
            name1=request.POST['name1']
            id1=request.POST['id1']
            name2=request.POST['name2']
            id2=request.POST['id2']
            name3=request.POST['name3']
            id3=request.POST['id3']
            name4=request.POST['name4']
            id4=request.POST['id4']
            name5=request.POST['name5']
            id5=request.POST['id5']
            name6=request.POST['name6']
            id6=request.POST['id6']
            name7=request.POST['name7']
            id7=request.POST['id7']
            name8=request.POST['name8']
            id8=request.POST['id8']
            name9=request.POST['name9']
            id9=request.POST['id9']
            name10=request.POST['name10']
            id10=request.POST['id10']
            name11=request.POST['name11']
            id11=request.POST['id11']
            name12=request.POST['name12']
            id12=request.POST['id12']
            name13=request.POST['name13']
            id13=request.POST['id13']
            user=Volleyball(teamname=teamname,
                         dept=dept,
                         coachname=coachname,
                         dept2=dept2,
                         captainname=captainname,
                         cid=cid,
                         name1=name1,
                         id1=id1,
                         name2=name2,
                         id2=id2,
                         name3=name3,
                         id3=id3,
                         name4=name4,
                         id4=id4,
                         name5=name5,
                         id5=id5,
                         name6=name6,
                         id6=id6,                        
                         name7=name7,
                         id7=id7,
                         name8=name8,
                         id8=id8,
                         name9=name9,
                         id9=id9,
                         name10=name10,
                         id10=id10, 
                         name11=name11,
                         id11=id11,
                         name12=name12,
                         id12=id12,
                         name13=name13,
                         id13=id13,  

                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/volleyball_form.html')

def kabaddi_form(request):
        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            coachname=request.POST['coachname']
            dept2=request.POST['dept2']
            captainname=request.POST['captainname']
            cid=request.POST['cid']
            name1=request.POST['name1']
            id1=request.POST['id1']
            name2=request.POST['name2']
            id2=request.POST['id2']
            name3=request.POST['name3']
            id3=request.POST['id3']
            name4=request.POST['name4']
            id4=request.POST['id4']
            name5=request.POST['name5']
            id5=request.POST['id5']
            name6=request.POST['name6']
            id6=request.POST['id6']
            name7=request.POST['name7']
            id7=request.POST['id7']
            name8=request.POST['name8']
            id8=request.POST['id8']
            name9=request.POST['name9']
            id9=request.POST['id9']
            name10=request.POST['name10']
            id10=request.POST['id10']
            name11=request.POST['name11']
            id11=request.POST['id11']
            name12=request.POST['name12']
            id12=request.POST['id12']
            name13=request.POST['name13']
            id13=request.POST['id13']
            user=Kabaddi(teamname=teamname,
                         dept=dept,
                         coachname=coachname,
                         dept2=dept2,
                         captainname=captainname,
                         cid=cid,
                         name1=name1,
                         id1=id1,
                         name2=name2,
                         id2=id2,
                         name3=name3,
                         id3=id3,
                         name4=name4,
                         id4=id4,
                         name5=name5,
                         id5=id5,
                         name6=name6,
                         id6=id6,                        
                         name7=name7,
                         id7=id7,
                         name8=name8,
                         id8=id8,
                         name9=name9,
                         id9=id9,
                         name10=name10,
                         id10=id10, 
                         name11=name11,
                         id11=id11,
                         name12=name12,
                         id12=id12,
                         name13=name13,
                         id13=id13,  

                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/kabaddi_form.html')

def video_form(request):

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
            name4=request.POST['name4']
            id4=request.POST['id4']
            name5=request.POST['name5']
            id5=request.POST['id5']
            user=Video(teamname=teamname,
                           dept=dept,
                           captainname=captainname,
                           cid=cid,
                           name1=name1,
                           id1=id1,
                           name2=name2,
                           id2=id2,
                           name3=name3,
                           id3=id3,
                           name4=name4,
                           id4=id4,
                           name5=name5,
                           id5=id5
                           )
                           

            user.save()
            return render(request,'app/AllCards.html')


        return render(request,'app/video_form.html')

def pc3_form(request):

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
            user=PC3(teamname=teamname,
                           dept=dept,captainname=captainname,
                           cid=cid,
                           name1=name1,
                           id1=id1,
                           name2=name2,
                           id2=id2,
                           name3=name3,
                           id3=id3)
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/pc3_form.html')

def badminton_form(request):

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
            user=Badminton(teamname=teamname,
                           dept=dept,captainname=captainname,
                           cid=cid,
                           name1=name1,
                           id1=id1,
                           name2=name2,
                           id2=id2,
                           name3=name3,
                           id3=id3)
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/badminton_form.html')


def chess_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=Chess(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')


        return render(request,'app/chess_form.html')

def highjump_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=HighJump(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/highjump_form.html')

def pc1_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=PC1(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/pc1_form.html')

def math_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=Math(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/math_form.html')

def ict_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=ICT(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/ict_form.html')

def rubkis_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=Rubkis(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/rubiks_form.html')

def table_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=Table(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/table_form.html')

def sprint_form(request):

        if request.method == 'POST':
            teamname=request.POST['teamname']
            dept=request.POST['dept']
            captainname=request.POST['captainname']
            cid=request.POST['cid']


            user=Sprint(teamname=teamname,
                         dept=dept,
                         captainname=captainname,
                         cid=cid,   
                         )
            user.save()
            return render(request,'app/AllCards.html')

        return render(request,'app/sprint_form.html')


def shedule(request):
     return render(request,'app/shedule.html')

def shedule_cricket(request):
     team=Cricket.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}
     return render(request,'app/shedule_cricket.html',context)


def shedule_football(request):
     team=Football.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}    
     return render(request,'app/shedule_football.html',context)

def shedule_volleyball(request):
     team=Volleyball.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}  
     return render(request,'app/shedule_volleyball.html',context)

def shedule_kabaddi(request):
     team=Kabaddi.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}    
     return render(request,'app/shedule_kabaddi.html',context)

def shedule_badminton(request):
     team=Badminton.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}
     return render(request,'app/shedule_badminton.html',context)

def shedule_table(request):
     team=Table.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}
     return render(request,'app/shedule_table.html',context)

def shedule_chess(request):
     team=Chess.objects.all()
     time=Time_shedule.objects.all()
     final=Semi_Final.objects.all()
     context={'team':team, 'time':time,'final':final}
     return render(request,'app/shedule_chess.html',context)







def shedule_highjump(request):
     team=HighJump.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_highjump.html',context)

def shedule_pc1(request):
     team=PC1.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_pc1.html',context)

def shedule_pc3(request):
     team=PC3.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_pc3.html',context)

def shedule_math(request):
     team=Math.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_math.html',context)

def shedule_ict(request):
     team=ICT.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_ict.html',context)

def shedule_video(request):
     team=Video.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_video.html',context)

def shedule_sprint(request):
     team=Sprint.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_sprint.html',context)

def shedule_rubiks(request):
     team=Rubkis.objects.all()
     time=Time_shedule.objects.all()
     context={'team':team ,'time':time}
     return render(request,'app/shedule_rubiks.html',context)

def score(request):
     team=home_score.objects.all()
     context={'team':team}
     return render(request,'app/score.html',context)

def score_all(request):
     team=home_score.objects.all()
     context={'team':team}
     return render(request,'app/score_all.html',context)






