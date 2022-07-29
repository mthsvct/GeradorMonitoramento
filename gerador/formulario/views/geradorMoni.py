import copy
import json
import datetime as dt
from dateutil import rrule
import random
import os

class Gerador():

    def __init__(self, indice=0, pasta=None, intervalo=15, result=None, case=0, date_initial=None, date_final=None):
        self.date_initial = date_initial #...... Data inicial do monitoramento
        self.date_final = date_final #.......... Data final do monitoramento
        self.name_app = None #.................. Nome do app;
        self.microsservices = None #............ Microsserviços extraídos do arquivo result;
        self.pasta = pasta #.................... Pasta onde será salvo o caminho;
        self.case = case #...................... Caso a ser gerado que será selecionado na função selectCase()
        self.result = result #.................. Aqui estarão os dados do arquivo resultData.json 
        self.intervalo = intervalo #............ Intervalo em minutos, setado em 15 minutos.
        self.indice = indice #.................. Indice onde o app se encontra no vetor presente no arquivo results
        self.arquivos = {
            'Pasta': '',
            'NomesArqs': [] 
        } #..................................... Aqui serão salvos as informações sobre os arquivos de salvamento.

    def abreArq(self):
        # Função que abre o arquivo result e transfere seus dados aos atributos da classe
        """ self.result = loadFile('resultData.json')[self.indice] """
        self.name_app = self.result["App"]
        self.microsservices = [ i for i in self.result['Resultados'] ] # For que coloca os Micro