from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

def selCaso(request):

    casos = [
        'Todos os requisitos serão atendidos.',
        'Nenhum dos requisitos serão atendidos.',
        'Os dados serão gerado aleatóreamente.',
    ]

    ms = request.session['selecoes']['selecionado']['Resultados']

    return render(request, 'selCaso.html', {'casos': casos, 'ms': ms})

def validaCaso(request):
    requisitosSelecionados = []

    if 'disponibilidade' in request.POST:
        requisitosSelecionados.append(1)

    if 'custo' in request.POST:
        requisitosSelecionados.append(2)

    if 'tempoResposta' in request.POST:
        requisitosSelecionados.append(3)

    return HttpResponse('Hello World!')

