from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        user=User.objects.create_user(username=username,password=password,email=email)
        login(request,user)
        return redirect("/dashboard/")
    return render(request,"signup.html")


def signin(request):
    context = {}
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect("/dashboard/")
        else:
            context['error']="Provide valid credentials!!"
            return render(request,'login.html',context)
    return render(request,"login.html",context)

def signout(request):
    logout(request)
    return redirect("/login/")
