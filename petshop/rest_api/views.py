from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

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

