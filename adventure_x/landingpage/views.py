from django.http.response import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import UserForm
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
    
    context = {}
    return render(request, 'index.html', context)

def startgame(request):
    user = User.objects.latest('date_added')
    return render(request, 'startgame.html', {"user":user})