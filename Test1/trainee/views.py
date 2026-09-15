from django.shortcuts import render
from django.http import HttpResponse
from .models import trainees

# Create your views here.
def allTrainees(request):
    context = {'trainees': trainees.objects.all()}
    return render(request, 'trainee/Trainees.html', context = context)

def insertTrainee(request):
    if request.method == 'POST':
        ptname = request.POST['tname']
        ptemail = request.POST['temail']
        ptphono = request.POST['tnum']
        trainees.objects.create(name = ptname, email = ptemail, phono = ptphono)
    return render(request, 'trainee/insert.html')

def removeTrainee(request, id):
    return HttpResponse(f"<h1>Remove Trainee number {id}</h1>")

def findTrainee(request, id):
    return HttpResponse(f"<h1>Search for Trainee number {id}</h1>")