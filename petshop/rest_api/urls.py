from django.urls import path

from rest_framework.routers import SimpleRouter
#from petshop.rest_api.serializers import AgendamentoModelSerializer
#import rest_api.views
from rest_api.views import AgendamentoModelViewSet, hello_world, test_lucas, AnimalCategoriaView, CategoriaModelViewSet

from rest_api.views import PetShopModelViewSet ##att m7 semana2(não precisa adicionar eu acho, depois checar a duvida da atividade da semana)
app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)
router.register('petshop', PetShopModelViewSet)
router.register('categoria', CategoriaModelViewSet)



urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
    path('test_lucas', test_lucas),
    path('animais/categoria/', AnimalCategoriaView.as_view('get')),
]

urlpatterns += router.urls