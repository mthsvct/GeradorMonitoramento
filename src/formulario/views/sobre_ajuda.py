from django.shortcuts import redirect, render
from django.http import HttpResponse

def sobre(request):
    return render(request, 'sobre.html')

def ajuda(request):
    return HttpResponse('Hello World!')

