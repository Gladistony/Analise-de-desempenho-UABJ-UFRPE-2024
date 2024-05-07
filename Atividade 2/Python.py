import time

inicial = time.time()
#Ler dados do txt
def ler_entrada(nome):
    arq = open(nome, 'r')
    dat = arq.readlines()
    arq.close()
    return dat
#Definir No
class No:
    def __init__(self, numero):
        self.numero = numero
        self.ponteiro = None
    def set_ponteiro(self, ponteiro):
        self.ponteiro = ponteiro
    def get_ponteiro(self):
        return self.ponteiro
    def get_numero(self):
        return self.numero
#Definir Lista
class L_Ligada:
    def __init__(self):
        self.cabeca = None
    def adicionar(self, numero, posicao):
        novo = No(numero)
        if self.cabeca == None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            for i in range(posicao-1):
                if atual.get_ponteiro() == None:
                    break
                atual = atual.get_ponteiro()
            novo.set_ponteiro(atual.get_ponteiro())
            atual.set_ponteiro(novo)
    def remover(self, numero):
        if self.cabeca == None:
            return -1
        if self.cabeca.get_ponteiro() == None:
            self.cabeca = None
            return -1
        atual = self.cabeca
        while atual.get_ponteiro() != None:
            if atual.get_ponteiro().get_numero() == numero:
                atual.set_ponteiro(atual.get_ponteiro().get_ponteiro())
                return 1
            atual = atual.get_ponteiro()
    def imprimir(self):
        lista = []
        atual = self.cabeca
        while atual != None:
            lista.append(atual.get_numero())
            atual = atual.get_ponteiro()
        print(lista)
# Processar dados
def processar_dados(caminho):
    dadosArquivo = ler_entrada(caminho)
    numeros = dadosArquivo[0].split()
    totalEntradas = int(dadosArquivo[1])
    comandos = []
    for i in range(2, totalEntradas+2):
        comandos.append(dadosArquivo[i].split())
    lista = L_Ligada()
    for dat in numeros:
        lista.adicionar(int(dat), 999)
    for cmd in comandos:
        if cmd[0] == 'A':
            if len(cmd) == 2:
                lista.adicionar(int(cmd[1]), 0)
            else:
                lista.adicionar(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'R':
            lista.remover(int(cmd[1]))
        elif cmd[0] == 'P':
            lista.imprimir()

processar_dados("Testes/arq-novo.txt")

tempo_total = time.time() - inicial
print("Tempo total: ", tempo_total)
