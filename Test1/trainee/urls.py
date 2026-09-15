from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all/', allTrainees, name="allTrainees"),
    path('insert/', insertTrainee, name='insertTrainee'),
    path('remove/<int:id>/', removeTrainee, name='removeTrainee'),
    path('search/<int:id>/', findTrainee, name='findTrainee'),
]