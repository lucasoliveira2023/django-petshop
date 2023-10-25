from django.shortcuts import render
from base.forms import ReservaBanhoForm
from base.forms import Reserva_pet_form
# Create your views here.
def inicio(request):
    return render(request ,'inicio.html')

def contato(request):
    return  render(request, 'contato.html')
##modulo 6 semana 2 atividade linhas 10 a 20
def reserva_banho(request):
    if request.method == 'POST':
        form = ReservaBanhoForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request, 'reserva/sucesso.html')
    else:
        form = ReservaBanhoForm()
    return render(request, 'reserva_banho.html', {'form': form})

##modulo6 semana3 ativiadade
def fazer_reserva(request):
    if request.method == 'POST':
        form = Reserva_pet_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reserva_sucesso.html')
    else:
        form = Reserva_pet_form()
    return render(request, 'reserva_banho.html', {'form': form})
