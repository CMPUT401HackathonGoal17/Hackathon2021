from django.urls import path

from . import views

urlpatterns = [
    path('g11q1/', views.q1, name='g11q1'),
    path('g11q2/', views.q2, name='g11q2'),
]
