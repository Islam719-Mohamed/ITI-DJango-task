from django.shortcuts import render, redirect
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
        ptpfp = request.FILES.get('tpfp')
        trainees.objects.create(name = ptname, email = ptemail, phono = ptphono, pfp = ptpfp)
    return render(request, 'trainee/insert.html')

def removeTrainee(request, id):
    trainees.objects.filter(id = id).delete()
    return redirect('/trainee/all/')

def findTrainee(request, id):
    context = {'trn': trainees.objects.get(id = id)}
    if request.method == 'POST':
        pname = request.POST['tuname']
        pemail = request.POST['tuemail']
        pphono = request.POST['tunum']
        trainees.objects.filter(id = id).update(name = pname, email = pemail, phono = pphono)
        return redirect('/trainee/all/')
    return render(request, 'trainee/update.html', context = context)