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
    path('cricket_rule/',views.cricket_rule,name="cricket_rule"),
    path('football_rule/',views.football_rule,name="football_rule"),
    path('highjump_rule/',views.highjump_rule,name="highjump_rule"),
    path('pc3_rule/',views.pc3_rule,name="pc3_rule"),
    path('kabaddi_rule/',views.kabaddi_rule,name="kabaddi_rule"),
    path('pc1_rule/',views.pc1_rule,name="pc1_rule"),
    path('math_rule/',views.math_rule,name="math_rule"),
    path('video_rule/',views.video_rule,name="video_rule"),
    path('ict_rule/',views.ict_rule,name="ict_rule"),
    path('rubiks_rule/',views.rubiks_rule,name="rubiks_rule"),
    path('table_rule/',views.table_rule,name="table_rule"),
    path('volleyball_rule/',views.volleyball_rule,name="volleyball_rule"),
    path('sprint_rule/',views.sprint_rule,name="sprint_rule"),

    path('cricket_form/',views.cricket_form,name="cricket_form"),
    path('football_form/',views.football_form,name="football_form"),
    path('volleyball_form/',views.volleyball_form,name="volleyball_form"),
    path('kabaddi_form/',views.kabaddi_form,name="kabaddi_form"),
]