from django.http.response import HttpResponse
from django.shortcuts import render

def q1(request):
    
    return render(request, 'q1.html', {})

def q2(request):
    return render(request, 'q2.html', {})

def q3(request):
    return render(request, 'q3.html', {})