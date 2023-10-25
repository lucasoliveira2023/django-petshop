from django import forms 
from .models import Reserva_pet
class ContatoForm(forms.Form):
    nome =forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
    
##modulo 6 semana2 atividade
class ReservaBanhoForm(forms.Form):
    nome_pet = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length = 15)
    dia_reserva = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    observacoes =forms.CharField(widget=forms.Textarea)
    
##modulo 6 semana3 atividaade
class Reserva_pet_form(forms.ModelForm):
    class Meta:
        model = Reserva_pet
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']