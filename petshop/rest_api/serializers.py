from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
from rest_framework import serializers
from reserva.models import Reserva, Petshop
from rest_api.models import Pet, Categoria, Animal       #ATT MODULO7 SEMANA2, e semana4
from datetime import date, datetime

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
    
    
#atividade m7 semana4
class CategoriaRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = CategoriaNestedModelSerializer
        super().__init__(**kwargs)
        
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    
class CategoriaNestedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriaModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name= 'api: reserva-detail'
    )
    
    class Meta:
        model = Categoria
        fields = '__all__'

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset = Petshop.objects.all(),
        read_only = False
    )
    categoria = CategoriaRelatedFieldCustomSerializer(
        queryset = Categoria.objects.all(),
        read_only = False
    )
    def validate_data(self, value): ##o today esta dando pau por algum motivo
        hoje = date.today()
        if value < hoje:
            raise ValidationError('Não é possivel realizar um agendamento para o passado!')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'


class AnimalSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'