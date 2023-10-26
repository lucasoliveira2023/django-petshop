from django.shortcuts import render
from base.forms import ReservaBanhoForm
from base.forms import ReservaPetForm

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
            return render(request, 'reserva_sucesso.html')
    else:
        form = ReservaBanhoForm()
    return render(request, 'reserva_banho.html', {'form': form})

##modulo6 semana3 ativiadade,,, revisar a atividade da semana 3 ta duplicado kkk
def fazer_reserva(request):
    if request.method == 'POST':
        form = ReservaPetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reserva_sucesso.html')
    else:
        form = ReservaPetForm()
    return render(request, 'reserva_banho.html', {'form': form})
