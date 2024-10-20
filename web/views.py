from django.shortcuts import render
from web.models import Agenda, LocalFotos, Fotos
# Create your views here.


def home(request): #função que ira direcionar a url para o arquivo html
    
    return render(request, 'index.html')


def qs_view(request):
    return render(request, 'quemSomos.html')


def mu_i_view(request):
    return render(request, 'mundo_imaginario.html')


def oe_view(request):
    return render(request, 'outrosEspetaculos.html')

def midia_view(request):
    midia = Fotos.objects.filter(local=2) 
    return render(request, 'midia.html', {'midia': midia})    


def teatro_view(request):
    teatro = Fotos.objects.filter(local=3) 
    return render(request, 'teatro.html', {'teatro': teatro})


def escola_view(request):
    escola = Fotos.objects.filter(local=1) 
    return render(request, 'escola.html', {'escola': escola})


def agenda_view(request):
    agenda = Agenda.objects.all()
    return render(request,
     'agenda.html',
     {'agenda': agenda})


def contato_view(request):
    return render(request, 'contatos.html')


def blog_view(request):
    return render(request, 'blog.html')