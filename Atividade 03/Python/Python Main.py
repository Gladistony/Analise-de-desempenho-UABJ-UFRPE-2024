import time
from memory_profiler import profile


LOCALENTRADA = "Entrada/arq.txt"
LOCALSAIDA = "Saida/arq-saida.py.txt"
MEMORYLOG = "Saida/memory.log.py.txt"

#Carrega o arquivo e salvar em uma array
file = open(LOCALENTRADA, "r")
dados = file.readlines()
file.close()
for i in range(len(dados)):
    dados[i] = int(dados[i])

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

#Criar lista com a contagem dos tempos de execução e quando de ran foi preciso para executar a função 
temposbubble = []
temposquick = []
log_file = open(MEMORYLOG, "w")

@profile(stream=log_file)
def medicaotempocommemoria(funcao, array, local):
    inicio = time.time()
    funcao(array.copy())
    fim = time.time()
    tempo = fim - inicio
    local.append(tempo)
    print("Tempo: " + str(tempo) + " s")

def medicaoTempo(funcao, array, local, qt):
    #Pegar o uso de memória da primeira execução
    medicaotempocommemoria(funcao, array, local)
    for i in range(qt-1):
        inicio = time.time()
        funcao(array.copy())
        fim = time.time()
        tempo = fim - inicio
        local.append(tempo)
        print("Tempo: " + str(tempo) + " s")

#Medir o tempo de execução e a quantidade de ram usada
medicaoTempo(bubbleSort, dados, temposbubble, 10)
medicaoTempo(quickSort, dados, temposquick, 10)
#Ordenar array
dados = quickSort(dados)

#Salvar os resultados em um arquivo
file = open("Saida/python.log.txt", "w")
file.write("BubbleSort\n")
for i in range(len(temposbubble)):
    file.write(str(temposbubble[i]) + "\n")
file.write("QuickSort\n")
for i in range(len(temposquick)):
    file.write(str(temposquick[i]) + "\n")
file.close()

#Salvar os resultados em um arquivo
file = open(LOCALSAIDA, "w")
for i in range(len(dados)):
    file.write(str(dados[i]) + "\n")
file.close()

log_file.close()
print("Fim")