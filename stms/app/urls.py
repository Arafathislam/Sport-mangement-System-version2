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
    path('video_form/',views.video_form,name="video_form"),
    path('pc3_form/',views.pc3_form,name="pc3_form"),
    path('badminton_form/',views.badminton_form,name="badminton_form"),
    path('chess_form/',views.chess_form,name="chess_form"),
    path('pc1_form/',views.pc1_form,name="pc1_form"),
    path('math_form/',views.math_form,name="math_form"),
    path('ict_form/',views.ict_form,name="ict_form"),
    path('rubkis_form/',views.rubkis_form,name="rubkis_form"),
    path('table_form/',views.table_form,name="table_form"),
    path('sprint_form/',views.sprint_form,name="sprint_form"),
    path('highjump_form/',views.highjump_form,name="highjump_form"),
    

    path('shedule/',views.shedule,name="shedule"),
    path('shedule_cricket/',views.shedule_cricket,name="shedule_cricket"),
    path('shedule_football/',views.shedule_football,name="shedule_football"),
    path('shedule_kabaddi/',views.shedule_kabaddi,name="shedule_kabaddi"),
    path('shedule_volleyball/',views.shedule_volleyball,name="shedule_volleyball"),
    path('shedule_table/',views.shedule_table,name="shedule_table"),
    path('shedule_chess/',views.shedule_chess,name="shedule_chess"),
    path('shedule_badminton/',views.shedule_badminton,name="shedule_badminton"),
    path('shedule_highjump/',views.shedule_highjump,name="shedule_highjump"),
    path('shedule_pc1/',views.shedule_pc1,name="shedule_pc1"),
    path('shedule_pc3/',views.shedule_pc3,name="shedule_pc3"),
    path('shedule_video/',views.shedule_video,name="shedule_video"),
    path('shedule_math/',views.shedule_math,name="shedule_math"),
    path('shedule_ict/',views.shedule_ict,name="shedule_ict"),
    path('shedule_sprint/',views.shedule_sprint,name="shedule_sprint"),
    path('shedule_rubiks/',views.shedule_rubiks,name="shedule_rubiks"),
    path('score/',views.score,name="score"),
    path('score_all/',views.score_all,name="score_all"),
]