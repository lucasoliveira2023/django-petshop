from datetime import date
import pytest 
from model_bakery import baker 

from reserva.models import Reserva, Petshop


@pytest.fixture
def reserva():
    data = date(2022, 8, 30)
    reserva = baker.make(
        Reserva,
        nome ='TOM',
        data=data,
        turno='tarde'
    )
    return reserva

@pytest.mark.django_db
def test_str_reservas_retorna_string_formatada():
    data = date(2024, 1, 30)
    reserva = baker.make(
        Reserva,
        nome = 'Tom',
        data =data,
        turno = 'Tarde'
    )

    assert str(reserva) == 'Tom : 2024-01-30 - Tarde'

@pytest.mark.django_db
def test_quant_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quant = 3
    baker.make(
        Reserva,
        quant,
        petshop = petshop
    )

    assert petshop.qtd_reservas() == 3