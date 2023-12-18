from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reserva.models import Reserva
from rest_api.serializers import AgendamentoModelSerializer, PetshopModelSerializer

##att modulo 7 semana2
from .models import Pet, Categoria, Animal
from .models import *
from .serializers import PetSerializer, CategoriaModelSerializer, AnimalSerialiser

# Create your views here.

#modulo7 semana3
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
    
#modulo 7 semana4
class PetShopModelViewSet(ReadOnlyModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]   
    
    
class CategoriaModelViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]   
    
    
        
## att modulo7 semana4
class AnimalCategoriaView(ModelViewSet):
    serializer_class = AnimalSerialiser
    
    def get_queryset(self):
        id_categoria = self.kwargs['categoria_id']
        return Animal.objects.filter(categoria=id_categoria)