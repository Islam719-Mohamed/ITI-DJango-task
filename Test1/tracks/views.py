from django.shortcuts import render, redirect
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
    tracks.objects.filter(id = id).update(status = False)
    return redirect('/tracks/all/')

def findTrack(request, id):
    return HttpResponse(f"<h1>Search for Track {id}</h1>")