from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..forms import UploadFile
import json

def uploadFile(request):
    arq = UploadFile()
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




