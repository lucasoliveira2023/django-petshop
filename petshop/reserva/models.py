from django.db import models

# Create your models here.
class Reserva(models.Model):
    TAMANHO_OPCOES = (
        (0, 'Pequeno'),
        (1, 'Medio'),
        (2, 'Grande'),
    )
    TURNO_OPCOES = (
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='Email')
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    data = models.DateField(verbose_name='Data', help_text='dd/mm/yyyy')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    tamanho = models.IntegerField(verbose_name='Tamanho',choices=TAMANHO_OPCOES)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.nome} : {self.data} - {self.turno}'
    
    class Meta:
        verbose_name ='Reserva de Banho'
        verbose_name_plural = 'Reserva de Banhos'