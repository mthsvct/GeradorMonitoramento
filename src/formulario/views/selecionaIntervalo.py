from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

def selIntervalo(request):

    intervalos = [
        {'time': '15 minutos', 'idI': 15},
        {'time': '1 vez por dia', 'idI': 1},
        {'time': '30 minutos', 'idI': 30},
        {'time': '2 vezes por dia', 'idI': 2},
        {'time': '1 hora', 'idI': 60},
    ]

    return render(request, 'selIntervalo.html', {
        'intervalos': intervalos
        }
    )

def validaIntervalo(request):
    b = request.POST['intervalo']
    intIntervalo = int(b)
    print(request.session['selecoes'].keys())

    if intIntervalo == 1:
        intervalo = 1440 # 1 vez por dia
    elif intIntervalo == 2:
        intervalo = 720 # 2 Vezes por dia
    elif intIntervalo == -1:
        intervalo = int(request.POST['minutagem']) # Personalizado
    else:
        intervalo = intIntervalo # 15 minutos, 30 minutos, 1 hr

    request.session['selecoes'] = {
        'apps': request.session['selecoes']['apps'], 
        'selecionado': request.session['selecoes']['selecionado'],
        'periodo': request.session['selecoes']['periodo'],
        'intervalo': intervalo
    }

    return redirect('selCaso')
