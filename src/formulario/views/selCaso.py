import datetime as dt
import enum
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import Http404
import os
from .geradorMoni import Gerador
import json
from .oficial import gerador

def selCaso(request):

    casos = [
        'Todos os requisitos serão atendidos.',
        'Nenhum dos requisitos serão atendidos.',
        'Os dados serão gerado aleatóreamente.',
    ]

    ms = request.session['selecoes']['selecionado']['Resultados']
    status = request.GET.get('status')
    return render(request, 'selCaso.html', {'status': status, 'casos': casos, 'ms': ms})

def recolheRequisitos(requestPost):
    requisitosSelecionados = []
    if 'disponibilidade' in requestPost: # Dá pra fazer uma função para esses IFs
        requisitosSelecionados.append(1)

    if 'custo' in requestPost:
        requisitosSelecionados.append(2)

    if 'tempoResposta' in requestPost:
        requisitosSelecionados.append(3)

    return requisitosSelecionados

def recolheMS(requestPost, microsservicos):
    ms = []
    for index, i in enumerate(microsservicos):
        if (f'ms{index}') in requestPost:
            ms.append(index)
    return ms

def validaCaso(request):

    caso = int(request.POST['caso'])
    selecao = {'caso': caso, 'requisito': None, 'ms': None}
        
    if caso == 4:
        selecao['requisito'] = recolheRequisitos(requestPost=request.POST)
    elif caso == 5:
        ms = recolheMS(requestPost=request.POST, microsservicos=request.session['selecoes']['selecionado']['Resultados'])

        if len(ms) > 0:
            selecao['ms'] = ms
        else:
            return redirect('/selCaso/?status=1')

    request.session['selecoes'] = {
        'apps': request.session['selecoes']['apps'], 
        'selecionado': request.session['selecoes']['selecionado'],
        'periodo': request.session['selecoes']['periodo'],
        'intervalo': request.session['selecoes']['intervalo'],
        'caso': selecao
    }
    
    montaGerador(request)

    return redirect('selDownload')


def download(request, idG, nome='resultData.json'):
    # Esta função baixa um arquivo
    file_path = os.path.join(settings.MEDIA_ROOT, str(idG), nome)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def montaGerador(request):

    result = request.session['selecoes']['selecionado']

    splitInicio = request.session['selecoes']['periodo']['inicial'].split('-')
    splitFinal = request.session['selecoes']['periodo']['final'].split('-')
    inicio = dt.datetime(year=int(splitInicio[0]), month=int(splitInicio[1]), day=int(splitInicio[2]))
    final = dt.datetime(year=int(splitFinal[0]), month=int(splitFinal[1]), day=int(splitFinal[2]))

    intervalo = int(request.session['selecoes']['intervalo'])

    caso = {
        'caso': int(request.session['selecoes']['caso']['caso']),
        'requisito': request.session['selecoes']['caso']['requisito'],
        'ms': request.session['selecoes']['caso']['ms']
    }

    gerador.case = caso['caso']
    gerador.intervalo = intervalo
    gerador.result = result
    gerador.date_initial = inicio
    gerador.date_final = final
    gerador.requisitos_selecionados = caso['requisito']
    gerador.ms_selecionados = caso['ms']

    gerador.abreArq()
    gerador.abrirArqDados()
    gerador.vaiProCaso()
    gerador.montar()
    gerador.salvarArqGestao()
    




