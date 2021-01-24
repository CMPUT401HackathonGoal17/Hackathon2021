from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render

#advenure_x/ending/template/ending.html
def index(request):
    context = {}
    
    return render(request, 'index.html', context)

def ending(request):

    return render(request, 'ending.html', {})
