from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from landingpage.models import User
from .models import UserGoal1

def q1(request):
    # users = UserGoal1.objects.order_by('id')
    # print(users)
    return render(request, 'g1q1.html', {})

def q2(request):
    return render(request, 'g1q2.html', {})

def q3(request):
    if request.method=="POST":
        return redirect('/goal4/q1')
    return render(request, 'g1q3.html', {})