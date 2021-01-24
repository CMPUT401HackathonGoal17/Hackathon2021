
from django.urls import path, include
from . import views

urlpatterns = [
    path('g7q1/', views.g7q1, name='g7q1'),
    path('g7q2/', views.g7q2, name='g7q2'),
    path('g7q3/', views.g7q3, name='g7q3'),
]
