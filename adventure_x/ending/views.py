from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render

#advenure_x/ending/template/ending.html
def end(request):
    context = {}
    
    return render(request, 'end.html', context)

def ending(request):

    return render(request, 'ending.html', {})
