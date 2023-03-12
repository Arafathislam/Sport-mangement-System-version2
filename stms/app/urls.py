from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('allcards/',views.allcards,name="allcards"),
    path('register/',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('tournament/',views.tournament,name="tournament"),
    path('news/',views.news,name="news"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('badmintion_rule/',views.badminton_rule,name="badmintion_rule"),
    path('chess_rule/',views.chess_rule,name="chess_rule"),
]