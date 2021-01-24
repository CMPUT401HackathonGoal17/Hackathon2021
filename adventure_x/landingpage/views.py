from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('startgame')
    else:
        context = {}
        return render(request, 'index.html', context)

def startgame(request):
    users = User.objects.order_by('id')
    if users.count() >= 1:
        user = users.last() # get the latest user
        return redirect('/goal1/g1q1')
    else:
        if request.method == "POST":
            return redirect('/goal1/g1q1')
        return render(request, 'startgame.html', {"user":"Guest"})