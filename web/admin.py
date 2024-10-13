from django.contrib import admin
from web.models import Agenda
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'local', 'descricao')
    search_fields = ('data', 'local', 'descricao')

admin.site.register(Agenda, AgendaAdmin)
