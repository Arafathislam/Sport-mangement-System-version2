from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name="home"),
    path('allcards/',views.allcards,name="allcards"),
    path('register/',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
]