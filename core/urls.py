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
    path('mundo_imaginario/', v.mu_i_view, name='mundo_imaginario'),
    path('outros_espetaculos/', v.oe_view, name='outros_espetaculos'),
    path('midia/', v.midia_view, name='midia'),
    path('teatro/', v.teatro_view, name='teatro'),
    path('escola/', v.escola_view, name='escola'),
    path('agenda/', v.agenda_view, name='agenda'),
    path('contato/', v.contato_view, name='contato'),
    path('blog/', v.blog_view, name='blog'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
