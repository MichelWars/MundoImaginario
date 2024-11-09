from django.shortcuts import render
from web.models import Agenda, LocalFotos, Fotos, youtube_link_video
from django.utils import timezone
# Create your views here.


def home(request): #função que ira direcionar a url para o arquivo html
    
    return render(request, 'index.html')


def qs_view(request):
    return render(request, 'quemSomos.html')


def espetaculos_view(request):
    return render(request, 'espetaculos.html')


def peca1_view(request):
    return render(request, 'peca1.html')

def peca2_view(request):
    return render(request, 'peca2.html')

def peca3_view(request):
    return render(request, 'peca3.html')

def midia_view(request):
    midia = Fotos.objects.filter(local=2)
    video = youtube_link_video.objects.all() 
    return render(request, 'midia.html', {'video': video, 'midia': midia})    


def teatro_view(request):
    teatro = Fotos.objects.filter(local=3) 
    return render(request, 'teatro.html', {'teatro': teatro})


def escola_view(request):
    escola = Fotos.objects.filter(local=1) 
    return render(request, 'escola.html', {'escola': escola})


def agenda_view(request):
    hoje = timezone.now().date()
    agenda = Agenda.objects.filter(data__gte=hoje).order_by('data')
    return render(request,
     'agenda.html',
     {'agenda': agenda})


def contato_view(request):
    return render(request, 'contatos.html')


def blog_view(request):
    return render(request, 'blog.html')