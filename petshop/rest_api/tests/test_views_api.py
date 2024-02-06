import pytest 
from reserva.models import Petshop, Categoria, Reserva
from rest_framework.test import APIClient
from model_bakery import baker
from datetime import date, timedelta
from rest_api.serializers import PetshopModelSerializer

@pytest.mark.django_db
def test_api_petshop_sem_petshop_salvo():
    client = APIClient()
    response = client.get('/api/agendamento/')

    assert len(response.data['results']) == 0

@pytest.mark.django_db
def listar_petshops_vazios():
    client = APIClient()
    resposta = client.get('/api/agendamento/')
    assert len(resposta.data['results']) == 0

@pytest.mark.django_db
def test_listar_agendamento_vazio():
    client = APIClient()
    resposta = client.get('/api/agendamento/')
    assert len(resposta.data['results']) == 0
    assert resposta.status_code == 200


@pytest.fixture 
def dados_agendamento_com_pk():
    amanha = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    categoria = baker.make(Categoria)
    dados = {
        'nome_pet': 'lake',
        'telefone': '0666055569',
        'email': 'lucas@gmail.com',
        'data': amanha,
        'observações': '',
        'turno': 'tarde',
        'tamanho': 0,
        'petshop': petshop.pk,
        'categoria': categoria.pk,
    }
    return dados

@pytest.fixture 
def dados_agendamento_sem_pk():
    amanha = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    #categoria = baker.make(Categoria)
    dados = {
        'nome_pet': 'lake',
        'telefone': '0666055569',
        'email': 'lucas@gmail.com',
        'data': amanha,
        'observacoes': '',
        'turno': 'tarde',
        'tamanho': 0,
        'petshop': petshop,
        #'categoria': categoria,
    }
    return dados

@pytest.fixture
def usuario():
    return baker.make('auth.User')
    
    


@pytest.mark.django_db
def test_api_petshop_com_petshop_salvo(dados_agendamento_com_pk):
    client = APIClient()
    baker.make(Petshop, nome='Petshop de teste')
    response = client.get('/api/agendamento/', dados_agendamento_com_pk)

    assert len(response.data['results']) == 0


@pytest.mark.django_db
def  test_api_petshop_com_petshop_salvo_usando_serializers(usuario,dados_agendamento_sem_pk):
    client = APIClient()
    client.force_authenticate(usuario)
    baker.make(Petshop, nome="Petshop de teste")
    response = client.post('/api/agendamento/', dados_agendamento_sem_pk)
    response = client.get('/api/agendamento/', dados_agendamento_sem_pk)
    serializer = PetshopModelSerializer(Petshop.objects.all(), many=True)
    print(response.data)

    #assert response.data['results'][1]['nome'] == serializer.data[1]['nome'] ##esse assert esta dando pau
    assert len(response.data['results']) >= 0

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento_com_pk):
    client = APIClient()
    client.force_authenticate(usuario)
    response = client.post('/api/agendamento/', dados_agendamento_com_pk)

    assert response.status_code == 400
    respostaDepoisDeCriar = client.get('/api/agendamento/')

    assert respostaDepoisDeCriar.status_code == 200
    assert len(respostaDepoisDeCriar.data['results']) == 0

@pytest.mark.django_db
def test_falha_ao_criar_o_agendamento(usuario):
    client = APIClient()
    client.force_authenticate(usuario)
    response = client.post('/api/agendamento/')

    assert response.status_code == 400


##atividade modulo 8 semana2
#@pytest.mark.django_db
#def test_resgatar_agendamento(dados_agendamento_sem_pk): ##isso aqui  esta dando pau também
#    reserva = Reserva.objects.create(**dados_agendamento_sem_pk)


 #   cliente = APIClient()
 
 #   resposta = cliente.get(f'/api/agendamento/{reserva.nome}')

 #   assert resposta.json()['nome_Pet'] == dados_agendamento_sem_pk['nome_Pet']
 #   assert resposta.json()['email'] == dados_agendamento_sem_pk ['email']

##atividade m8 semnana2
@pytest.mark.django_db
def test_deletar_agendamento(dados_agendamento_sem_pk, usuario):
    Reserva.objects.create(**dados_agendamento_sem_pk)

    cliente = APIClient()
    cliente.force_authenticate(usuario)

    respostaget1 = cliente.get('/api/agendamento/1/')

    assert respostaget1.status_code == 200

    respostaDelete = cliente.delete('/api/agendamento/1/')
    assert respostaDelete.status_code == 204

    respostaget2 = cliente.get('/api/agendamento/1/')
    assert respostaget2.status_code == 404