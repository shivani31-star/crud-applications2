from django.shortcuts import render,redirect
from .models import *
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email exists")
        else:
            User.objects.create(name=name , email=email , password=password)
            return redirect('/login/')
        
def login(request):
    return render(request,'login.html')

def table(request):
    data = User.objects.all()
    return render(request,'table.html',{"data" : data})

def update_view(request,uid):
    res = User.objects.get(id=uid)
    return render(request,'update.html',{"data" : res})

def update_form(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['name']
        email = request.POST['email']
        User.objects.filter(id=uid).update(name=name , email=email)
        return redirect("/table/")
    
def delete(request,pk):
    User.objects.filter(id=pk).delete()
    return redirect("/table/")
