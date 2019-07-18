from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'index.html')

def hotplace(request) :
    return render(request, 'hotplace.html')

def convin(request) :
    return render(request, 'convin.html')