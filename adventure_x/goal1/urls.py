from django.urls import path

from . import views

urlpatterns = [
    path('g1q1/', views.g1q1, name='g1q1'),
    path('g1q2/', views.g1q2, name='g1q2'),
    path('g1q3/', views.g1q3, name='g1q3'),
]
