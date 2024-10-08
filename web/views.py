from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request): #função que ira direcionar a url para o arquivo html
    
    return render(request, 'index.html')