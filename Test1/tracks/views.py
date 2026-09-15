from django.shortcuts import render
from django.http import HttpResponse
from .models import tracks

# Create your views here.
def allTrack(request):
    context = {'tracks': tracks.objects.all()}
    return render(request, 'tracks/tracks.html', context=context)

def insertTrack(request):
    if request.method == 'POST':
        pcname = request.POST['cname']
        tracks.objects.create(course = pcname)
    return render(request, 'tracks/insert.html')

def removeTrack(request, id):
    return HttpResponse(f"<h1>Remove Track {id}</h1>")

def findTrack(request, id):
    return HttpResponse(f"<h1>Search for Track {id}</h1>")