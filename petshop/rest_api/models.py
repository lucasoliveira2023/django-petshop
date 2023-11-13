from django.db import models

# Create your models here.
#atividade da m7 semana 2
class Pet(models.Model):
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    data = models.DateField(verbose_name='Data', help_text='dd/mm/yyyy')
    email = models.EmailField(verbose_name='Email')
    