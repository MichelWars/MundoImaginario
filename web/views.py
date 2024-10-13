from django.shortcuts import render
from web.models import Agenda
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
    return render(request, 'midia.html')    


def teatro_view(request):
    return render(request, 'teatro.html')


def escola_view(request):
    return render(request, 'escola.html')


def agenda_view(request):
    agenda = Agenda.objects.all()
    return render(request,
     'agenda.html',
     {'agenda': agenda})


def contato_view(request):
    return render(request, 'contatos.html')


def blog_view(request):
    return render(request, 'blog.html')