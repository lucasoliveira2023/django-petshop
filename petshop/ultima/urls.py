"""
URL configuration for ultima project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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