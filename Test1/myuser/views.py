from django.shortcuts import render
from django.http import HttpResponse
from .models import user

# Create your views here.
def home(request):
    return render(request , 'myuser/home.html')

def login(request):
    users = user.objects.all()
    if request.method == 'POST':
        puname = request.POST['usrname']
        ppassword = request.POST['usrpass']
        for usr in users:
            print(usr)
            if(puname == usr.uname and ppassword == usr.password):
                return HttpResponse(f'<b>Welcome {usr.fname} {usr.lname}, you were born on {usr.birthdate}</b>')
    
    return render(request, 'myuser/Login.html')

def signup(request):
    if request.method == 'POST':
        puname = request.POST['usrname']
        pfname = request.POST['fname']
        plname = request.POST['lname']
        pbirthdate = request.POST['usrbd']
        ppassword = request.POST['usrpass']
        user.objects.create(uname = puname, fname = pfname, lname = plname, birthdate = pbirthdate, password = ppassword)
    
    return render(request, 'myuser/signup.html')

def signout(request):
    return HttpResponse("<h1>SignOut Page</h1>")