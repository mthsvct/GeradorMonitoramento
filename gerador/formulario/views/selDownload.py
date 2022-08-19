import datetime as dt
from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
from django.http import Http404
from .oficial import gerador

def selDownload(request):
    return render(request, 'selDownload.html', {
        'resultados_gerados': gerador.resultados_gerados,
        'idG': gerador.id
        }
    )


