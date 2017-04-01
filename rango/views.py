from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(Request):
    return HttpResponse("Rango says hello world")

