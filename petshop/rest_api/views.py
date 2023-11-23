from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reserva.models import Reserva
from rest_api.serializers import AgendamentoModelSerializer

##att modulo 7 semana2
from .models import Pet 
from .serializers import PetSerializer

# Create your views here.

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] #isso aqui é se eu quiser que apenas os autenticados acessem--modulo7semana3
    #permission_classes = [IsAuthenticatedOrReadOnly]



@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})

    return Response({'hello': 'World API'})

##atividade da m7semana1 criar views, não entendi muito bem acho que é isso

@api_view(['GET', 'POST'])
def test_lucas(request):
    if request.method == 'GET':
        return Response({'message': f'bem-vindo dev, {request.data.get("name")}'})
    
    return Response({'ola':'world API'})


##att modulo7 semaana 2

class PetsModelViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer