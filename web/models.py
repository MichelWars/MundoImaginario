from django.db import models

# Create your models here.
class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descricao