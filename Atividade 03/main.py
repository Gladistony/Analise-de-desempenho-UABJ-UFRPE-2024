import matplotlib.pyplot as plt
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#Coletar dados do processo em java
file = open("Saida/java.log.txt", "r")
temposjava = file.readlines()
file.close()
file = open("Saida/memory.log.java.txt", "r")
memoriajava = file.readlines()
file.close()
#Coletar dados do processo em python
file = open("Saida/python.log.txt", "r")
tempospython = file.readlines()
file.close()
file = open("Saida/memory.log.py.txt", "r")
memoriapython = file.readlines()
file.close()
#Analisar os dados das duas linguagens
java = {"BubbleSort": [], "QuickSort": []}
javaBMemoria = 0
javaQMemoria = 0
python = {"BubbleSort": [], "QuickSort": []}
pythonBMemoria = 0
pythonQMemoria = 0
#Tempos em java
id = 0
for i in temposjava:
    if is_number(i):
        #Converter ns em segundos
        i = float(i) / 1000000000
        if id < 10:
            id += 1
            java["BubbleSort"].append(float(i))
        else:
            java["QuickSort"].append(float(i))
#Tempos em python
id = 0
for i in tempospython:
    if is_number(i):
        #Converter ms em segundos
        if id < 10:
            id += 1
            python["BubbleSort"].append(float(i))
        else:
            python["QuickSort"].append(float(i))
#Extrair a memória utilizada em java
totalB = 0
totalQ = 0
id = 0
for i in memoriajava:
    if id < 10:
        totalB += abs(float(i))
    else:
        totalQ += abs(float(i))
    id += 1
javaBMemoria = totalB / 10
javaQMemoria = totalQ / 10
#converter de byte para megabyte
javaBMemoria = javaBMemoria / 1048576
javaQMemoria = javaQMemoria / 1048576
#extrair a memória utilizada em python
totalB = 24.3
totalQ = 24.1
#Media e mediana dos tempos
mediaJavaB = sum(java["BubbleSort"]) / 10
mediaJavaQ = sum(java["QuickSort"]) / 10
mediaPythonB = sum(python["BubbleSort"]) / 10
mediaPythonQ = sum(python["QuickSort"]) / 10
medianaJavaB = sorted(java["BubbleSort"])[4]
medianaJavaQ = sorted(java["QuickSort"])[4]
medianaPythonB = sorted(python["BubbleSort"])[4]
medianaPythonQ = sorted(python["QuickSort"])[4]
#Criar um grafico dos tempos em java
def criarGrafico(lista, nome, titulo):
    tamanho = len(lista)
    plt.plot(range(1, tamanho + 1), lista)
    plt.xlabel("Execução")
    plt.ylabel("Tempo (s)")
    plt.title(titulo)
    plt.savefig("Graficos/" + nome + ".png")
    plt.clf()

criarGrafico(java["BubbleSort"], "javaBubbleSort", "BubbleSort em Java")
criarGrafico(java["QuickSort"], "javaQuickSort", "QuickSort em Java")
criarGrafico(python["BubbleSort"], "pythonBubbleSort", "BubbleSort em Python")
criarGrafico(python["QuickSort"], "pythonQuickSort", "QuickSort em Python")

#Refazer graficos em python excluindo o primeiro valor
criarGrafico(python["BubbleSort"][1:], "pythonBubbleSort2", "BubbleSort em Python")
criarGrafico(python["QuickSort"][1:], "pythonQuickSort2", "QuickSort em Python")

#Criar um arquivo com as descrições da media, mediana e total de memoria usada
file = open("Saida/descricao.txt", "w")
file.write("Analise dos dados\n")
file.write("Linguagem Java\n")
file.write("\nBubbleSort\n\n")
file.write("Media: " + str(mediaJavaB) + "\n")
file.write("Mediana: " + str(medianaJavaB) + "\n")
file.write("Memoria: " + str(javaBMemoria) + " MB\n")
file.write("\nQuickSort\n\n")
file.write("Media: " + str(mediaJavaQ) + "\n")
file.write("Mediana: " + str(medianaJavaQ) + "\n")
file.write("Memoria: " + str(javaQMemoria) + " MB\n")
file.write("\n")
file.write("Linguagem Python\n")
file.write("\nBubbleSort\n\n")
file.write("Media: " + str(mediaPythonB) + "\n")
file.write("Mediana: " + str(medianaPythonB) + "\n")
file.write("Memoria: " + str(totalB) + " MB\n")
file.write("\nQuickSort\n\n")
file.write("Media: " + str(mediaPythonQ) + "\n")
file.write("Mediana: " + str(medianaPythonQ) + "\n")
file.write("Memoria: " + str(totalQ) + " MB\n")
file.close()
