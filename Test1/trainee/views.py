from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def insertTrainee(request):
    return HttpResponse("<h1>Insert a Trainee</h1>")

def removeTrainee(request):
    return HttpResponse("<h1>Remove a Trainee</h1>")

def findTrainee(request):
    return HttpResponse("<h1>Search for a Trainee</h1>")