from django.contrib import admin
from django.urls import path, include

from base.views import inicio, contato, reserva_banho
from reserva.views import criar_reserva

urlpatterns = [
    path('', inicio),
    path('contato/', contato, name='contato'),
    path('reserva/', include('reserva.urls'), name='reserva'),
    path('reserva_banho/', reserva_banho, name='reserva_banho'),##att m6s2 importando da views a função criada chamada reserva_banho
    path('criar_reserva/', criar_reserva, name='fazer_reserva'),##att m6s3 importando da views a função criada chamada fazer_reserva
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls', namespace='api')),
]