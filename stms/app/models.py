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


class Video(models.Model):


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
    name4=models.CharField(max_length=20)
    id4=models.IntegerField()
    name5=models.CharField(max_length=20)
    id5=models.IntegerField()

    def __str__(self):
        return self.teamname



class PC3(models.Model):


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


    def __str__(self):
        return self.teamname





class Cricket(models.Model):


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
    coachname=models.CharField(max_length=20)
    dept2=models.CharField(max_length=20)
    cid=models.IntegerField()
    name1=models.CharField(max_length=20)
    id1=models.IntegerField()
    name2=models.CharField(max_length=20)
    id2=models.IntegerField()
    name3=models.CharField(max_length=20)
    id3=models.IntegerField()
    name4=models.CharField(max_length=20)
    id4=models.IntegerField()
    name5=models.CharField(max_length=20)
    id5=models.IntegerField()
    name6=models.CharField(max_length=20)
    id6=models.IntegerField()
    name7=models.CharField(max_length=20)
    id7=models.IntegerField()
    name8=models.CharField(max_length=20)
    id8=models.IntegerField()
    name9=models.CharField(max_length=20)
    id9=models.IntegerField()
    name10=models.CharField(max_length=20)
    id10=models.IntegerField()
    name11=models.CharField(max_length=20)
    id11=models.IntegerField()
    name12=models.CharField(max_length=20)
    id12=models.IntegerField()
    name13=models.CharField(max_length=20)
    id13=models.IntegerField()


    def __str__(self):
        return self.teamname
    

class Football(models.Model):


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
    coachname=models.CharField(max_length=20)
    dept2=models.CharField(max_length=20)
    cid=models.IntegerField()
    name1=models.CharField(max_length=20)
    id1=models.IntegerField()
    name2=models.CharField(max_length=20)
    id2=models.IntegerField()
    name3=models.CharField(max_length=20)
    id3=models.IntegerField()
    name4=models.CharField(max_length=20)
    id4=models.IntegerField()
    name5=models.CharField(max_length=20)
    id5=models.IntegerField()
    name6=models.CharField(max_length=20)
    id6=models.IntegerField()
    name7=models.CharField(max_length=20)
    id7=models.IntegerField()
    name8=models.CharField(max_length=20)
    id8=models.IntegerField()
    name9=models.CharField(max_length=20)
    id9=models.IntegerField()
    name10=models.CharField(max_length=20)
    id10=models.IntegerField()
    name11=models.CharField(max_length=20)
    id11=models.IntegerField()
    name12=models.CharField(max_length=20)
    id12=models.IntegerField()
    name13=models.CharField(max_length=20)
    id13=models.IntegerField()


    def __str__(self):
        return self.teamname
    

class Kabaddi(models.Model):


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
    coachname=models.CharField(max_length=20)
    dept2=models.CharField(max_length=20)
    cid=models.IntegerField()
    name1=models.CharField(max_length=20)
    id1=models.IntegerField()
    name2=models.CharField(max_length=20)
    id2=models.IntegerField()
    name3=models.CharField(max_length=20)
    id3=models.IntegerField()
    name4=models.CharField(max_length=20)
    id4=models.IntegerField()
    name5=models.CharField(max_length=20)
    id5=models.IntegerField()
    name6=models.CharField(max_length=20)
    id6=models.IntegerField()
    name7=models.CharField(max_length=20)
    id7=models.IntegerField()
    name8=models.CharField(max_length=20)
    id8=models.IntegerField()
    name9=models.CharField(max_length=20)
    id9=models.IntegerField()
    name10=models.CharField(max_length=20)
    id10=models.IntegerField()
    name11=models.CharField(max_length=20)
    id11=models.IntegerField()
    name12=models.CharField(max_length=20)
    id12=models.IntegerField()
    name13=models.CharField(max_length=20)
    id13=models.IntegerField()


    def __str__(self):
        return self.teamname
    


class Volleyball(models.Model):


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
    coachname=models.CharField(max_length=20)
    dept2=models.CharField(max_length=20)
    cid=models.IntegerField()
    name1=models.CharField(max_length=20)
    id1=models.IntegerField()
    name2=models.CharField(max_length=20)
    id2=models.IntegerField()
    name3=models.CharField(max_length=20)
    id3=models.IntegerField()
    name4=models.CharField(max_length=20)
    id4=models.IntegerField()
    name5=models.CharField(max_length=20)
    id5=models.IntegerField()
    name6=models.CharField(max_length=20)
    id6=models.IntegerField()
    name7=models.CharField(max_length=20)
    id7=models.IntegerField()
    name8=models.CharField(max_length=20)
    id8=models.IntegerField()
    name9=models.CharField(max_length=20)
    id9=models.IntegerField()
    name10=models.CharField(max_length=20)
    id10=models.IntegerField()
    name11=models.CharField(max_length=20)
    id11=models.IntegerField()
    name12=models.CharField(max_length=20)
    id12=models.IntegerField()
    name13=models.CharField(max_length=20)
    id13=models.IntegerField()


    def __str__(self):
        return self.teamname
    

class Chess(models.Model):


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

    def __str__(self):
        return self.teamname
    

class HighJump(models.Model):


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

    def __str__(self):
        return self.teamname
    

class PC1(models.Model):


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

    def __str__(self):
        return self.teamname
    


class Math(models.Model):


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

    def __str__(self):
        return self.teamname
    

class ICT(models.Model):


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

    def __str__(self):
        return self.teamname
    

class Rubkis(models.Model):


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

    def __str__(self):
        return self.teamname
    

class Table(models.Model):


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

    def __str__(self):
        return self.teamname
    

class Sprint(models.Model):


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

    def __str__(self):
        return self.teamname
    

class Contact(models.Model):
     
     fname=models.CharField(max_length=20)
     lname=models.CharField(max_length=20)
     email=models.EmailField(max_length=50,unique=True)
     mobile=models.CharField(max_length=20)
     msg=models.CharField(max_length=200)


     def __str__(self):
         return self.fname

# time shedule for first round
class Time_shedule(models.Model):
        cricket_time=models.CharField(max_length=200,blank=True)
        football_time=models.CharField(max_length=200,blank=True)
        volleyball_time=models.CharField(max_length=200,blank=True)
        kabaddi_time=models.CharField(max_length=200,blank=True)
        chess_time=models.CharField(max_length=200,blank=True)
        highjump_time=models.CharField(max_length=200,blank=True)
        pc1_time=models.CharField(max_length=200,blank=True)
        math_time=models.CharField(max_length=200,blank=True)
        ict_time=models.CharField(max_length=200,blank=True)
        rubiks_time=models.CharField(max_length=200,blank=True)
        table_time=models.CharField(max_length=200,blank=True)
        sprint_time=models.CharField(max_length=200,blank=True)
        badminton_time=models.CharField(max_length=200,blank=True)
        pc3_time=models.CharField(max_length=200,blank=True)
        video_time=models.CharField(max_length=200,blank=True)

# s1/s2/s3/s4 team name and st1/st2 time
class Semi_Final(models.Model):
    cricket_team1=models.CharField(max_length=200,blank=True)
    cricket_team2=models.CharField(max_length=200,blank=True)
    cricket_time1=models.CharField(max_length=200,blank=True)
    cricket_team3=models.CharField(max_length=200,blank=True)
    cricket_team4=models.CharField(max_length=200,blank=True)
    cricket_time2=models.CharField(max_length=200,blank=True)
    cricket_finalteam1=models.CharField(max_length=200,blank=True)
    cricket_finalteam2=models.CharField(max_length=200,blank=True)
    cricket_finaltime=models.CharField(max_length=200,blank=True)

    football_team1=models.CharField(max_length=200,blank=True)
    football_team2=models.CharField(max_length=200,blank=True)
    football_time1=models.CharField(max_length=200,blank=True)
    football_team3=models.CharField(max_length=200,blank=True)
    football_team4=models.CharField(max_length=200,blank=True)
    football_time2=models.CharField(max_length=200,blank=True)
    football_finalteam1=models.CharField(max_length=200,blank=True)
    football_finalteam2=models.CharField(max_length=200,blank=True)
    football_finaltime=models.CharField(max_length=200,blank=True)

    volleyball_team1=models.CharField(max_length=200,blank=True)
    volleyball_team2=models.CharField(max_length=200,blank=True)
    volleyball_time1=models.CharField(max_length=200,blank=True)
    volleyball_team3=models.CharField(max_length=200,blank=True)
    volleyball_team4=models.CharField(max_length=200,blank=True)
    volleyball_time2=models.CharField(max_length=200,blank=True)
    volleyball_finalteam1=models.CharField(max_length=200,blank=True)
    volleyball_finalteam2=models.CharField(max_length=200,blank=True)
    volleyball_finaltime=models.CharField(max_length=200,blank=True)

    kabaddi_team1=models.CharField(max_length=200,blank=True)
    kabaddi_team2=models.CharField(max_length=200,blank=True)
    kabaddi_time1=models.CharField(max_length=200,blank=True)
    kabaddi_team3=models.CharField(max_length=200,blank=True)
    kabaddi_team4=models.CharField(max_length=200,blank=True)
    kabaddi_time2=models.CharField(max_length=200,blank=True)
    kabaddi_finalteam1=models.CharField(max_length=200,blank=True)
    kabaddi_finalteam2=models.CharField(max_length=200,blank=True)
    kabaddi_finaltime=models.CharField(max_length=200,blank=True)

    chess_team1=models.CharField(max_length=200,blank=True)
    chess_team2=models.CharField(max_length=200,blank=True)
    chess_time1=models.CharField(max_length=200,blank=True)
    chess_team3=models.CharField(max_length=200,blank=True)
    chess_team4=models.CharField(max_length=200,blank=True)
    chess_time2=models.CharField(max_length=200,blank=True)
    chess_finalteam1=models.CharField(max_length=200,blank=True)
    chess_finalteam2=models.CharField(max_length=200,blank=True)
    chess_finaltime=models.CharField(max_length=200,blank=True)


    table_team1=models.CharField(max_length=200,blank=True)
    table_team2=models.CharField(max_length=200,blank=True)
    table_time1=models.CharField(max_length=200,blank=True)
    table_team3=models.CharField(max_length=200,blank=True)
    table_team4=models.CharField(max_length=200,blank=True)
    table_time2=models.CharField(max_length=200,blank=True)
    table_finalteam1=models.CharField(max_length=200,blank=True)
    table_finalteam2=models.CharField(max_length=200,blank=True)
    table_finaltime=models.CharField(max_length=200,blank=True)


    badminton_team1=models.CharField(max_length=200,blank=True)
    badminton_team2=models.CharField(max_length=200,blank=True)
    badminton_time1=models.CharField(max_length=200,blank=True)
    badminton_team3=models.CharField(max_length=200,blank=True)
    badminton_team4=models.CharField(max_length=200,blank=True)
    badminton_time2=models.CharField(max_length=200,blank=True)
    badminton_finalteam1=models.CharField(max_length=200,blank=True)
    badminton_finalteam2=models.CharField(max_length=200,blank=True)
    badminton_finaltime=models.CharField(max_length=200,blank=True)





class home_score(models.Model):
    score_desc=models.TextField(null=True, blank=True)
    upteam1=models.CharField(max_length=200,blank=True)
    upteam2=models.CharField(max_length=200,blank=True)
    upteam3=models.CharField(max_length=200,blank=True)
    upteam4=models.CharField(max_length=200,blank=True)
    upteam5=models.CharField(max_length=200,blank=True)
    upteam6=models.CharField(max_length=200,blank=True)
    uptime1=models.CharField(max_length=200,blank=True)
    uptime2=models.CharField(max_length=200,blank=True)
    uptime3=models.CharField(max_length=200,blank=True)

    fteam1=models.CharField(max_length=200,blank=True)
    fteam2=models.CharField(max_length=200,blank=True)
    fteam3=models.CharField(max_length=200,blank=True)
    fteam4=models.CharField(max_length=200,blank=True)
    fteam5=models.CharField(max_length=200,blank=True)
    fteam6=models.CharField(max_length=200,blank=True)
    ftime1=models.CharField(max_length=200,blank=True)
    ftime2=models.CharField(max_length=200,blank=True)
    ftime3=models.CharField(max_length=200,blank=True)

    carsol_pic1=models.ImageField(null=True,default="e.png")
    carsol_pic2=models.ImageField(null=True,default="w.png")
    carsol_pic3=models.ImageField(null=True,default="e.png")
    carsol_pic4=models.ImageField(null=True,default="w.png")
    carsol_pic5=models.ImageField(null=True,default="e.png")
    carsol_pic6=models.ImageField(null=True,default="w.png")

    dsc1=models.TextField(null=True, blank=True)
    dsc2=models.TextField(null=True, blank=True)
    dsc3=models.TextField(null=True, blank=True)

    day1=models.TextField(null=True, blank=True)
    day2=models.TextField(null=True, blank=True)
    day3=models.TextField(null=True, blank=True)

    time1=models.TextField(null=True, blank=True)
    time2=models.TextField(null=True, blank=True)
    time3=models.TextField(null=True, blank=True)


    


    





