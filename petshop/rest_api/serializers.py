from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from reserva.models import Reserva, Petshop
from rest_api.models import Pet, Categoria, Animal       #ATT MODULO7 SEMANA2, e semana4

#m7semaan4
class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

    class Meta:
        model = Petshop
        fields = '__all__'
class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'


class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopNestedModelSerializer(read_only=True)
    
    class Meta:
        model = Reserva
        fields = '__all__'
        
#ATT MODULO7 SEMANA2
class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        
#m7semana4
class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)
        
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    
class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )
    class Meta:
        model = Reserva
        fields = '__all__'
    
    
#atividade m7 semana4
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        field = '__all__'
        
class AnimalSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'