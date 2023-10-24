from django.shortcuts import render
from base.forms import ReservaBanhoForm
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
    return render(request, 'formulario_reserva.html', {'form': form})