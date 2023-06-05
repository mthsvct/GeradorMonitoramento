from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..forms import UploadFile
import json
from .oficial import gerador, restartGerador
from django.conf import settings
import os
import shutil

def uploadFile(request):
    arq = UploadFile()
    restartGerador(gerador)
    apagaPastas()
    return render(request, 'upload.html', { 'upload': arq } )


def validaFile(request):
    """ 
        Tem que verificar se é do tipo JSON
        Se possui a estrutura do arquivo Result
        Se não houver, logo deve ser direcionado para a mesma página com a mensagem de erro.
    """
    a = request.FILES['arq']
    apps = json.load(a)
    request.session['selecoes'] = {'apps': apps}
    return redirect('selApp')


def selApp(request):
    return render(request, 'selApps.html', {'selecoes': request.session['selecoes']})


def validaSelApp(request):
    i = int(request.POST['appSel'])
    request.session['selecoes'] = {'apps': request.session['selecoes']['apps'], 'selecionado': request.session['selecoes']['apps'][i]}
    return redirect('selPeriodo')


def apagaPastas():
    a = os.listdir(settings.MEDIA_ROOT)
    for index, i in enumerate(a):
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, i))

