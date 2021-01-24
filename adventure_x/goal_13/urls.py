from django.urls import path

from . import views

urlpatterns = [
	   path('', views.goal13, name='goal13'),
	   path('next/', views.next, name= 'next')
]
