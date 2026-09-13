from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def insertTrack(request):
    return HttpResponse("<h1>Insert a Track</h1>")

def removeTrack(request):
    return HttpResponse("<h1>Remove a Track</h1>")

def findTrack(request):
    return HttpResponse("<h1>Search for a Track</h1>")