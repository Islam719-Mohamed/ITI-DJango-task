from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all/', allTrack, name="allTrack"),
    path('insert/', insertTrack, name="insertTrack"),
    path('remove/<int:id>/', removeTrack, name="removeTrack"),
    path('search/<int:id>/', findTrack, name="findTrack"),
]
