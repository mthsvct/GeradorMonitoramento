from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

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

def validaPeriodo(request):
    a = request.POST['periodo']
    """ Verificar se:
            1 - [  ] O periodo selecionado em 'outros' possui a data inicial antes da data final 
            2 - [  ] Se o idP, que é a quantidade de dias selecionados, não for -1 então deve ser realizado a contagem da data.
    """
    return redirect('selIntervalo')





    