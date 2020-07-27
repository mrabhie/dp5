from django.shortcuts import render
from django.shortcuts import HttpResponse
from math import factorial

def index(request):
    return HttpResponse("<h1>welcome to views of dp5app</h1>")

def home(request):
    return render(request,"dp5app/main.html",{'pname':"abhilash"})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h1>factorial  of  value {} is:{}</h1>".format(n,factorial(n)))

def child(request):
    return render(request,"child.html")

