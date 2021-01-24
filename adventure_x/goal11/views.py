from django.http.response import HttpResponse
from django.shortcuts import render

def q1(request):
    context = {} 
    return render(request, 'g11q1.html', context)

def q2(request):
    context = {} 
    return render(request, 'g11q2.html', context)

def q3(request):
    context = {} 
    return render(request, 'g11q3.html', context)