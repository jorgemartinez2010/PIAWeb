from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'pagina.html',)

def pagina2(request):
    return render(request,'pagina2.html',)

def pagina3(request):
    return render(request,'pagina3.html',)

def pagina4(request):
    return render(request,'pagina4.html',)

def pagina5(request):
    return render(request,'pagina5.html',)