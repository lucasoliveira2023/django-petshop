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
    nome:str = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='Email')
    telefone = models.CharField(verbose_name= 'Telefone', max_length=100, null=True)
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    data = models.DateField(verbose_name='Data', help_text='dd/mm/yyyy')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    tamanho = models.IntegerField(verbose_name='Tamanho',choices=TAMANHO_OPCOES)
    observacoes = models.TextField(blank=True)
    petshop = models.ForeignKey(
        'Petshop', 
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null = True
        )
    categoria = models.ForeignKey(
        'Categoria',
        related_name = 'categorias',
        on_delete =models.CASCADE, 
        blank=True,
        null=True
    )
    def __str__(self):
        return f'{self.nome} : {self.data} - {self.turno}'
    
    class Meta:
        verbose_name ='Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'
        
        
class Petshop(models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Endereço', max_length=100)
    numero_da_residencia = models.CharField(verbose_name='Numero', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)
    
    
    def __str__(self):
        return f'Nome: {self.nome} - Endereço {self.rua}, {self.numero_da_residencia} - {self.bairro}'
    

class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria', max_length=50)
