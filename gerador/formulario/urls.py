from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', uploadFile, name='upload'),
    path('validaFile/', validaFile, name="validaFile"),
    path('selApp/', selApp, name="selApp"),
    path('validaSelApp/', validaSelApp, name="validaSelApp"),
    path('selPeriodo/', selPeriodo, name="selPeriodo"),
    path('validaPeriodo/', validaPeriodo, name="validaPeriodo"),
    path('selIntervalo/', selIntervalo, name="selIntervalo"),
    path('validaIntervalo/', validaIntervalo, name="validaIntervalo"),
    path('selCaso/', selCaso, name="selCaso"),
    path('validaCaso/', validaCaso, name="validaCaso"),
    path('download/', download, name="download"),
    path('selDownload/', selDownload, name="selDownload"),
]
