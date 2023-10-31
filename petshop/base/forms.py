from django import forms 
from base.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        
class ReservaBanhoForm(forms.Form):
    nome_pet = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=15)
    dia_reserva = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    observacoes = forms.CharField(widget=forms.Textarea)
