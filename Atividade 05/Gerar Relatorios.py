import matplotlib.pyplot as plt
import pandas as pd
import re

relatoriospython = ['Atividade 05/Tempos/Tempos Python Collab.txt', 'Atividade 05/Tempos/Tempos Python Google.txt', 'Atividade 05/Tempos/Tempos Python Meu Notebook.txt', 'Atividade 05/Tempos/Tempos Python Replit.txt']
relatoriosjava = ['Atividade 05/Tempos/Tempos Java Meu Notebook.txt', 'Atividade 05/Tempos/Tempos Java Replit Google.txt', 'Atividade 05/Tempos/Tempos Java Replit.txt']

def loadfile(name):
    with open(name, 'r') as file:
        return file.readlines()

#formato: bubbleSort - 0 - Tempo: 0.10535630048252642 ms - Memória: 270336 bytes
pattern = r"(\w+) - \d+ - Tempo: ([\d.e-]+) ms"
pattern2 = r"ria: (-?\d+) bytes"

informacoes = {}

for i in relatoriospython:
    lines = loadfile(i)
    dispositivo = i.split(' ')[-1].split('.')[0]
    for line in lines:
        result = re.search(pattern, line)
        result2 = re.search(pattern2, line)
        if result:
            nome = result.group(1)
            tempo = float(result.group(2))
            if result2:
                memoria = int(result2.group(1))
            else:
                memoria = 0
            if nome not in informacoes:
                informacoes[nome] = {}
            if dispositivo not in informacoes[nome]:
                informacoes[nome][dispositivo] = []
            informacoes[nome][dispositivo].append((tempo*1000, memoria))

#formato: Tempo BubbleSort: 2918382900 ns - Memória: 136013792 bytes
pattern = r"Tempo (\w+): (\d+) ns - Mem"
pattern2 = r"ria: (\d+) bytes"

informacoesjava = {}
for i in relatoriosjava:
    lines = loadfile(i)
    dispositivo = i.split(' ')[-1].split('.')[0]
    for line in lines:
        result = re.search(pattern, line)
        result2 = re.search(pattern2, line)
        if result:
            nome = result.group(1)
            tempo = float(result.group(2))/1000000
            if result2:
                memoria = int(result2.group(1))
            else:
                memoria = 0
            if nome not in informacoesjava:
                informacoesjava[nome] = {}
            if dispositivo not in informacoesjava[nome]:
                informacoesjava[nome][dispositivo] = []
            informacoesjava[nome][dispositivo].append((tempo, memoria))

def gerargraficos(lista, ling):
    for nome in lista:
        for dispositivo in lista[nome]:
            tempos = [x[0] for x in lista[nome][dispositivo]]
            memorias = [x[1] for x in lista[nome][dispositivo]]
            plt.plot(tempos, label=dispositivo)
            plt.title(nome)
            plt.xlabel('Execução')
            plt.ylabel('Tempo (ms)')
            plt.legend()
        plt.savefig(f'Atividade 05/Graficos/{nome}-{ling}.png')
        plt.clf()

gerargraficos(informacoes, 'Python')
gerargraficos(informacoesjava, 'Java')

# Calcular média e mediana dos tempos e memórias e incluir tudo num arquivo do excel
def calcular_estatisticas(lista):
    estatisticas = []
    for nome in lista:
        for dispositivo in lista[nome]:
            tempos = [x[0] for x in lista[nome][dispositivo]]
            memorias = [x[1] for x in lista[nome][dispositivo]]
            media_tempo = sum(tempos) / len(tempos)
            mediana_tempo = sorted(tempos)[len(tempos) // 2]
            media_memoria = sum(memorias) / len(memorias)
            mediana_memoria = sorted(memorias)[len(memorias) // 2]
            estatisticas.append({
                'Método': nome,
                'Dispositivo': dispositivo,
                'Média Tempo (ms)': media_tempo,
                'Mediana Tempo (ms)': mediana_tempo,
                'Média Memória (bytes)': media_memoria,
                'Mediana Memória (bytes)': mediana_memoria
            })
    return estatisticas

estatisticas_python = calcular_estatisticas(informacoes)
estatisticas_java = calcular_estatisticas(informacoesjava)

df_python = pd.DataFrame(estatisticas_python)
df_java = pd.DataFrame(estatisticas_java)

with pd.ExcelWriter('Atividade 05/Estatisticas_Tempos_Memorias.xlsx') as writer:
    df_python.to_excel(writer, sheet_name='Python', index=False)
    df_java.to_excel(writer, sheet_name='Java', index=False)