from django import forms 
from .models import ReservaPet
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
class ReservaPetForm(forms.ModelForm):
    class Meta:
        model = ReservaPet
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']