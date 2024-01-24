from django.core.management.base import BaseCommand

from reserva.models import Petshop
import random

class Command(BaseCommand):
    def lista_petshops(self):
        return Petshop.objects.all().values_list('pk', flat=True)

    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?',
            default=5,
            type=int,
            help='How many persons should be participate in the contest'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.lista_petshops(),
            help='Petshop ID to execute the constest'
        )

    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)

        return random.sample(banhos_list, quantidade)
    
    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.SUCCESS(
                'Dados do petshop que realizou o sorteio'
            )
        )
        self.stdout.write(f'Nome d Petshop: {petshop.nome}')
        self.stdout.write(
            f'Endereço:{petshop.nome} ,{petshop.rua}, {petshop.numero_da_residencia} - {petshop.bairro}'
        )

    def imprimir_reserva_sorteadas(self, reservas):
        #self.stdout.write(reservas)
        self.stdout.write(
            self.style.SUCCESS(
                'Dados das pessoas e animais sorteados'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                  '=' * 35
            )
        )
        for reserva in reservas:
            self.stdout.write(
                f'Animal: {reserva.nome_pet}'
            )
            self.stdout.write(
                f'Tutor: {reserva.nome} - {reserva.email}'
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    '=' * 35
                )
            )
    
    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']

        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()### da onde vem a função reservas, estou tendo o mesmo problema em models no reservas .count(models.py de reserva)
        
        banhos_escolhidos = self.escolher_reservas(reservas, quantity)
        
        self.stdout.write(
            self.style.SUCCESS('Sorteio concluido')
        )

        self.imprimir_info_petshop(petshop)
        self.imprimir_reserva_sorteadas(banhos_escolhidos)