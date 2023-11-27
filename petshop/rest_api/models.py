from django.db import models

# Create your models here.
#atividade da m7 semana 2
class Pet(models.Model):
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    data = models.DateField(verbose_name='Data', help_text='dd/mm/yyyy')
    email = models.EmailField(verbose_name='Email')
    
    
##atividade m7 semana4

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome_categoria
    
class Animal(models.Model):
    nome_animal = models.CharField(max_length=255)
    categoria_animal = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_de_entrada = models.DateField(verbose_name='Data', help_text='dd/mm/yyyy')
    email = models.EmailField(verbose_name='Email')