from rest_framework.serializers import ModelSerializer

from reserva.models import Reserva
from rest_api.models import Pet       #ATT MODULO7 SEMANA2

class AgendamentoModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
#ATT MODULO7 SEMANA2
class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'