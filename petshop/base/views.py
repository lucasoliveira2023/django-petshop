from django.shortcuts import render
from base.forms import ContatoForm
from base.forms import ReservaBanhoForm


# Create your views here.
def inicio(request):
    return render(request ,'inicio.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(68) 99220-8221 ',
        'responsavel': 'Lucas Oliveira França',
        'form': form,
        'sucesso': sucesso
    }
    return  render(request, 'contato.html', contexto)

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

