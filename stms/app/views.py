from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main.html')


def allcards(request):
    return render(request,'app/AllCards.html')




