import pytest
from model_bakery import baker 
from pytest_django.asserts import assertTemplateUsed
from datetime import  timedelta, date
from reserva.models import Reserva

@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')

@pytest.fixture
def dados_validos():
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome':'Joao',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'telefone':'9999-9999',
        'data':amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'o tom esta bem dedorento'
    }
    return dados


@pytest.mark.django_db
def test_reserva_view_retorna_sucesso(client, dados_validos):
    response = client.post('/reserva/criar/', dados_validos)
    print('\n test')
    print(response.content)
    assert response.status_code == 200
    assert 'Reserva realizada com sucesso' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
    client.post('/reserva/criar/', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']
    assert reserva.nome_pet == dados_validos['nome_pet']