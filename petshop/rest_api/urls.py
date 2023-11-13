from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import AgendamentoModelViewSet, hello_world, test_lucas
from rest_api.views import petsModelViewSet ##att m7 semana2(não precisa adicionar eu acho, depois checar a duvida da atividade da semana)
app_name = 'rest_api'

router = SimpleRouter()
router.register('agendamento', AgendamentoModelViewSet)

urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
    path('test_lucas', test_lucas),
]

urlpatterns += router.urls