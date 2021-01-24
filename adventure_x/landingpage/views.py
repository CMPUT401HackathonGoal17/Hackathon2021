from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('startgame')
    else:
        context = {}
        return render(request, 'index.html', context)

def startgame(request):
    users = User.objects.order_by('id')
    print(users)
    if users.count() >= 1:
        user = users.last() # get the latest user
        return render(request, 'startgame.html', {"user":user.name})
    else:
        return render(request, 'startgame.html', {"user":"Guest"})