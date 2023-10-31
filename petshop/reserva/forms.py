from datetime import date
from django import forms
from reserva.models import Reserva
#atividade da semana m6 semana4
class ReservaForm(forms.ModelForm):
    
    def clean_data(self):
        data = self.cleaned_data['date']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('impossivel fazer reserva para o passado')
        
        reserva_existem = Reserva.objects.filter(data=data).count()
        if reserva_existem >= 4:
            raise forms.ValidationError('ja existem 4 reservas para esta data. Por favor escolha outra data.')
        
        return data

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno',
            'tamanho', 'observacoes'
        ]