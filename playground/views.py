from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    #pull data from database
    #Transform data
    #Send email
    #return HttpResponse("Hello  World")
    x = calculate()
    return render(request, "hello.html", {'name': 'Aaqib', 'x': x})
    