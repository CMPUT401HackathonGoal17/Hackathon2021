"""adventure_x URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ending import views
from goal4 import views
from goal7 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('goal11/', include('goal11.urls')),
    path('goal1/', include('goal1.urls')),
    path('goal13/',include('goal_13.urls')),

    path('ending/', include('ending.urls')),
    path('goal4/', include('goal4.urls')),
    path('goal7/', include('goal7.urls')),
]
