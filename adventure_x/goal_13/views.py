from django.shortcuts import render

# Create your views here.

def goal13(request):
	return render(request, 'goal13.html', {})

def next(request):
	return render(request, 'next.html', {})
