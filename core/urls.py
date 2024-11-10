"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from web import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name='home'),
    path('quem_somos/', v.qs_view, name='quem_somos'), #parametros: nome da url e função importada da view
    path('espetaculos/', v.espetaculos_view, name='espetaculos'),
    path('peca1/', v.peca1_view, name='peca1'),
    path('peca2/', v.peca2_view, name='peca2'),
    path('peca3/', v.peca3_view, name='peca3'),
    path('peca4/', v.peca4_view, name='peca4'),
    path('midia/', v.midia_view, name='midia'),
    path('teatro/', v.teatro_view, name='teatro'),
    path('escola/', v.escola_view, name='escola'),
    path('agenda/', v.agenda_view, name='agenda'),
    path('contato/', v.contato_view, name='contato'),
    path('blog/', v.blog_view, name='blog'),
    path('post1/', v.post1_view, name='post1'),
    path('post2/', v.post2_view, name='post2'),
    path('post3/', v.post3_view, name='post3'),
    path('post4/', v.post4_view, name='post4'),
    path('post5/', v.post5_view, name='post5'),
    path('post6/', v.post6_view, name='post6'),
    path('post7/', v.post7_view, name='post7'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
