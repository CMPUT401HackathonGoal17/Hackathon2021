from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render('index.html')

def startgame(request):
    return HttpResponse("You have started the game")