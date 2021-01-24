from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('q2/', views.q2, name='q2'),
    path('q3/', views.q3, name='q3'),
]
