from Metodos import *
import pytest
import pytest_monitor

LOCALENTRADA = "Entrada/arq.txt"
LOCALSAIDA = "Saida/arq-saida.py.txt"

file = open(LOCALENTRADA, "r")
dados = file.readlines()
file.close()
for i in range(len(dados)):
    dados[i] = int(dados[i])

#Criar um array ordenado
dadosOrdenados = dados.copy()
dadosOrdenados.sort()


def test_bubbleSort():
    assert bubbleSort(dados.copy()) == dadosOrdenados

def test_quickSort():
    assert quickSort(dados.copy()) == dadosOrdenados