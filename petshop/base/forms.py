from django import forms 

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