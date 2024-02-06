from django.shortcuts import render
from django.http import HttpResponse
# Import the Category model
from rango.models import Category

def index(request):
    response = "Rango says hey there partner! "
    response += '<a href="{% url "rango:about" %}">About</a>'  
    return HttpResponse(response)

def about(request):
    return HttpResponse("Rango says here is the about page.")
