from datetime import date
from django import forms
from reserva.models import Reserva, Petshop
##atividade do modulo 6 semana4
class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno',
            'telefone','tamanho', 'petshop','observacoes','data'
        ]
        widget = {
            'DiadaReserva': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_data(self):
        data = self.cleaned_data['date']
        hoje = date.today()
        
        if data < hoje:
            raise forms.ValidationError('não é possivel realizar uma reserva para o passado!')
        
        numeroAtualdeReserva = Reserva.objects.filter(DiadaReserva=data).count()
        
        if numeroAtualdeReserva >=4:
            raise forms.ValidationError('ja existem muitas reservas para esse dia, por favor selecione outro dia')
        
        return data
    