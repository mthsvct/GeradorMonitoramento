from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime as dt

def selPeriodo(request):
    periodos = [
        {'time': '1 dia', 'idP':1},
        {'time': '2 semanas', 'idP':14},
        {'time': '2 dias', 'idP':2},
        {'time': '1 mês', 'idP':30},
        {'time': '1 semana', 'idP':7} 
    ]

    t = datetime.today().date()

    dia = f'0{t.day}' if t.day < 10 else f'{t.day}'
    mes = f'0{t.month}' if t.month < 10 else f'{t.month}'
    hoje = f'{t.year}-{mes}-{dia}'

    futuro = t.month + 3 # Aqui selecionei que o máximo é 3 meses de monitoramento.

    if futuro > 12:
        futuro = futuro - 12
        anoFuturo = t.year + 1
    else:
        anoFuturo = t.year
    
    mesFuturo = f'0{futuro}' if futuro < 10 else f'{futuro}'

    maximo = f'{anoFuturo}-{mesFuturo}-{dia}'

    return render(request, 'selPeriodo.html', {
        'selecoes': request.session['selecoes'], 
        'periodos': periodos, 
        'hoje': hoje,
        'maximo': maximo
        }
    )


def montaDatas(splitInicial, splitFinal):

    inicial = dt.datetime(
        year=int(splitInicial[0]), 
        month=int(splitInicial[1]), 
        day=int(splitInicial[2])
    )

    final = dt.datetime(
        year=int(splitFinal[0]), 
        month=int(splitFinal[1]), 
        day=int(splitFinal[2])
    )

    return {'inicial': inicial, 'final': final}


def validaPeriodo(request):
    
    periodo = int(request.POST['periodo'])

    if periodo == (-1):
        inicial = request.POST['DataInicial']
        final = request.POST['DataFinal']
    else:
        hoje = dt.date.today()
        passar = dt.timedelta(periodo)
        Dfinal = hoje + passar
        inicial = (f'{hoje.year}-{hoje.month}-{hoje.day}')
        final = (f'{Dfinal.year}-{Dfinal.month}-{Dfinal.day}')

    request.session['selecoes'] = {
        'apps': request.session['selecoes']['apps'], 
        'selecionado': request.session['selecoes']['selecionado'],
        'periodo': {'inicial': inicial, 'final': final}
    }

    return redirect('selIntervalo')


    