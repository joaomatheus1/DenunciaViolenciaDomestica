from django.db import models 

# Create your models here.
class Position(models.Model):
    tittle = models.CharField(max_length=50)

class Woman(models.Model):
    nome_completo = models.CharField(max_length=150)
    numero = models.CharField(max_length=11)
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)
    wom_code = models.CharField(max_length=50)
    descricao= models.TextField()
