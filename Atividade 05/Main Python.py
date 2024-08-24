import time
import os
import psutil

TOTALREPETICOES = 10

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quickSort([x for x in arr[1:] if x < arr[0]]) + arr[0:1] + quickSort([x for x in arr[1:] if x >= arr[0]])
#Carregar a array original
arrayOriginal = []
file = open("arq.txt", "r")
for line in file:
    arrayOriginal.append(int(line))
file.close()

class Resultados:
    def __init__(self, nome):
        self.horarioinicial = 0
        self.horariofinal = 0
        self.memoriainicial = 0
        self.memoriafinal = 0
        self.testnome = nome
    def sethora(self, inicio, fim):
        self.horarioinicial = inicio
        self.horariofinal = fim
    def setmemoria(self, inicio, fim):
        self.memoriainicial = inicio
        self.memoriafinal = fim
    def __str__(self):
        return self.testnome + " - Tempo: " + str(self.horariofinal - self.horarioinicial) + " ms - Memória: " + str(self.memoriafinal - self.memoriainicial) + " bytes"

def medirTempo(funcao, array):
    medicoes = []
    for i in range(TOTALREPETICOES):
        print("Execução " + str(i) + " de " + funcao.__name__)
        idprocesso = os.getpid()
        processo = psutil.Process(idprocesso)
        memoriainicio = processo.memory_info().rss
        tempoinicio = time.time() / 1000
        funcao(array.copy())
        memoriafim = processo.memory_info().rss
        tempofim = time.time() / 1000
        tempclass = Resultados(funcao.__name__ + " - " + str(i))
        tempclass.sethora(tempoinicio, tempofim)
        tempclass.setmemoria(memoriainicio, memoriafim)
        medicoes.append(tempclass)
    return medicoes

medidas = []
medidas += medirTempo(bubbleSort, arrayOriginal)
medidas += medirTempo(quickSort, arrayOriginal)
print("Resultados:")
for i in medidas:
    print(i) 
        