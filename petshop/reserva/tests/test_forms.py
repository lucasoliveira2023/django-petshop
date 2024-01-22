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
    Reserva.objects.create(data=data_hj)


    form_data = {'data': data_hj}
    form = ReservaForm(data=form_data) #a mesma coisa do de baixo

    assert  not form.is_valid()
    #assert'data'= form.errors
    assert  not form.errors['data'][0] == 'ja existe muitas reservas nesse dia, escolha outo'

@pytest.mark.django_db
def test_data_valida():
    data_futura = date.today() + timedelta(days=7)
    form_data = {'data':data_futura}
    form = ReservaForm(data=form_data)

    assert not form.is_valid()     ##forma negativa da função .is_valid()
