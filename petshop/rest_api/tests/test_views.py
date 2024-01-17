import pytest 
from reserva.models import Petshop
from rest_framework.test import APIClient
from model_bakery import baker
from rest_api.serializers import PetshopModelSerializer
from rest_framework import status



@pytest.mark.django_db
def test_api_petshop_sem_petshop_salvo():
    client = APIClient()
    response = client.get('/api/petshop')

    assert len(response.data['results']) == 0

@pytest.mark.django_db
def test_api_petshop_com_petshop_salvo():
    client = APIClient()
    baker.make(Petshop, nome='Petshop de teste')
    response = client.get('/api/petshop')

    assert len(response.data['results']) == 0


@pytest.mark.django_db
def  test_api_petshop_com_petshop_salvo_usando_serializers():
    client = APIClient()
    baker.make(Petshop, nome="Petshop de teste")
    response = client.get('/api/petshop')
    serializer = PetshopModelSerializer(Petshop.objects.all(), many=True)

    assert response.data['result'] == serializer.data


@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    client = APIClient()
    client.force_authenticate(usuario)
    response = client.post('/api/agendamento', dados_agendamento)

    assert response.status_code == 201

@pytest.mark.django_db
def test_falha_ao_criar_o_agendamento(usuario, dados_invalidos):
    client = APIClient()
    client.force_authenticate(usuario)
    response = client.post('/api/agendamento', dados_invalidos)

    assert response.status_code == 201

