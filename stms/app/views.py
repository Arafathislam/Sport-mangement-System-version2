from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main.html')


def login(request):
    return render(request,'app/login.html')


