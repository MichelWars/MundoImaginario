from django.contrib import admin

from web.models import Agenda, Fotos, LocalFotos, youtube_link_video

# Register your models here.


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'local', 'descricao')
    search_fields = ('data', 'local', 'descricao')


class LocalFotosAdmin(admin.ModelAdmin):
    list_display = ('local',)
    search_fields = ('local',)


class FotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem', 'legenda', 'local')
    search_fields = ('id', 'legenda', 'local__local')


class youtube_link_videoAdmin(admin.ModelAdmin):
    list_display = ('link', 'titulo')
    search_fields = ('id', 'titulo')


admin.site.register(Agenda, AgendaAdmin)
admin.site.register(LocalFotos, LocalFotosAdmin)
admin.site.register(Fotos, FotosAdmin)
admin.site.register(youtube_link_video, youtube_link_videoAdmin)
