from datetime import date, timedelta
import pytest 
from django.core.exceptions import ValidationError
from reserva.forms import ReservaForm
from reserva.models import Reserva

@pytest.mark.django_db
def test_data_passada():
    data_passada = date.today() - timedelta(days=1)
    form_data = {'data': data_passada}
    form = ReservaForm(data=form_data)

    assert not form.is_valid()
    assert form.is_valid() == False    ##a linha de cima é igual a de baixo
    

@pytest.mark.django_db
def test_muitas_reservas():
    data_hj = date.today()                    ##lembrando um teste para cada reserva então se tiver 4 reserva serão 4 Reserva.Objects.create
    data = {'nome':'lucas',
            'email':'lucas@email.com',
            'telefone': '999-9999',
            'nome_pet':'lake',
            'data': data_hj,
            'turno': 'manhã',
            'tamanho': 0,
            }
    
    Reserva.objects.create(**data)


    
    form = ReservaForm(data) #a mesma coisa do de baixo
    print(form.as_p())

    assert   form.is_valid()
    #assert'data'= form.errors
    

@pytest.mark.django_db
def test_data_valida():
    data_futura = date.today() + timedelta(days=7)
    data =  {'nome':'lucas',
            'email':'lucas@email.com',
            'telefone': '999-9999',
            'nome_pet':'lake',
            'data': data_futura,
            'turno': 'manhã',
            'tamanho': 0,
            }
    
    form_data = {'data':data}
    form = ReservaForm(data)

    assert  form.is_valid()     ##forma negativa da função .is_valid()
