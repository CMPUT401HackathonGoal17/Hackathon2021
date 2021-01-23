from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    
    return render(request, 'index.html', context)

def startgame(request):
    return HttpResponse("You have started the game")