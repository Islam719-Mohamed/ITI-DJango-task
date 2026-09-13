"""
URL configuration for Test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from myuser.views import *
from tracks.views import *
from trainee.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('signup/', signup),
    path('signout/', signout),
    path('tracks/insert/', insertTrack),
    path('tracks/remove/', removeTrack),
    path('tracks/search/', findTrack),
    path('trainees/insert/', insertTrainee),
    path('trainees/remove/', removeTrainee),
    path('trainees/search/', findTrainee),
]
