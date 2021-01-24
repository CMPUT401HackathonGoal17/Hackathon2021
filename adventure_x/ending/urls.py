from django.urls import path

from . import views

urlpatterns = [
    path('ending/', views.end, name='end')

]
