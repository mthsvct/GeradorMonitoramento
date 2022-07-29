from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render


def selIntervalo(request):

    intervalos = [
        {'time': '15 minutos', 'idI': 15},
        {'time': '1 hora', 'idI': 60},
        {'time': '30 minutos', 'idI': 30},
        {'time': '2 vezes por dia', 'idI': 2},
        {'time': '1 vez por dia', 'idI': 1}
    ]

    return render(request, 'selIntervalo.html', {
        'intervalos': intervalos
        }
    )

def validaIntervalo(request):
    b = request.POST['intervalo']
    c = int(b)
    return redirect('selCaso')
