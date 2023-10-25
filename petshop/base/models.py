from django.db import models

# Create your models here.
#atividade modulo6 semana3
class Reserva_pet(models.Model):
    nome_pet = models.CharField(max_length=100)
    telefone = models.CharField(max_length=51)
    dia_reserva = models.DateField()
    observacoes = models.TextField()
    
    def __str__(self):
        return self.nome_pet
    