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
    
    
class LocalFotos(models.Model):
    id = models.AutoField(primary_key=True)
    local = models.CharField(max_length=200)
    
    def __str__(self):
        return self.local
    
class Fotos(models.Model):
    id = models.AutoField(primary_key=True)
    legenda = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='web/', blank=False, null=False)
    local = models.ForeignKey(LocalFotos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.legenda