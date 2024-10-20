from django.contrib import admin
from web.models import Agenda, LocalFotos, Fotos
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'local', 'descricao')
    search_fields = ('data', 'local', 'descricao')
    
    
class LocalFotosAdmin(admin.ModelAdmin):
    list_display = ('local',)
    search_fields = ('local',)
    
    
class FotosAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'legenda', 'local')
    search_fields = ('legenda', 'local')

admin.site.register(Agenda, AgendaAdmin)
admin.site.register(LocalFotos, LocalFotosAdmin)
admin.site.register(Fotos, FotosAdmin)