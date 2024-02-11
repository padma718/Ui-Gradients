from django.http import HttpResponse
from django.shortcuts import render

from .models import registereddata1


# Create your views here.
def homep(request):
    return render(request, "main/project.html")

def multi(request):
    return render(request, "main/multi.html")

def bright(request):
    return render(request, "main/bright.html")

def premi(request):
    return render(request, "main/premium.html")
def reg(request):
    return render(request, "main/register.html")

def login(request):
    return render(request,"main/login.html")

def register(request):
    if request.method=="POST":
        if(request.POST.get("name") and request.POST.get("email") and request.POST.get("phno") and request.POST.get("passw") and
            request.POST.get("passw1")):
            register= registereddata1()
            register.name = request.POST.get("name")
            register.email = request.POST.get("email")
            register.phno = request.POST.get("phno")
            register.passw = request.POST.get("passw")
            register.passw1 = request.POST.get("passw1")
            register.save()
            return HttpResponse("""
            <html>
            <head>
            <title>Success</title>
            <style>
            #h{
            margin:323px;
            color:#097969;
            }
            </style>
            </head>
            <body style="background-color:#B2BEB5">
            <center><h1 id="h" >Registered Sucessfully!!! </h1></center>
            </body>
            </html>
            """)

        else:
            return HttpResponse("""
            <html>
            <head>
            <title>Success</title>
            <style>
            #h{
            margin:323px;
            color:#097969;
            }
            </style>
            </head>
            <body style="background-color:#B2BEB5">
            <center><h1 id="h" >Some fields are missing!!! </h1></center>
            </body>
            </html>
            """)
    form = registereddata1()
    return render(request, "main/register.html", context={"form":form})

