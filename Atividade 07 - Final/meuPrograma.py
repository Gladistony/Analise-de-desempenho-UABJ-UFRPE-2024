import sys
import os

def verifiacarNumero(valorString):
    try:
        int(valorString)
        return True
    except:
        return False

def operar(argumentos, id):
    #encontrar qual a operação buscando um dos parametros
    operacao = "@"
    for i in argumentos:
        if i in ["+", "-", "*", "/"]:
            operacao = i
            break
    numero1 = -1
    numero2 = -1
    #encontrar os numeros
    for i in range(len(argumentos)):
        if verifiacarNumero(argumentos[i]):
            numero1 = int(argumentos[i])
            argumentos.pop(i)
            break
    for i in range(len(argumentos)):
        if verifiacarNumero(argumentos[i]):
            numero2 = int(argumentos[i])
            argumentos.pop(i)
            break
    if numero1 == -1 or numero2 == -1 or operacao == "@":
        print("Argumentos inválidos!")
        return
    if operacao == "+":
        print(f"Resultado da opercação {id}: {numero1 + numero2}")
    elif operacao == "-":
        print(f"Resultado da opercação {id}: {numero1 - numero2}")
    elif operacao == "*":
        print(f"Resultado da opercação {id}: {numero1 * numero2}")
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: Divisão por zero!")
        else:
            print(f"Resultado da opercação {id}: {numero1 / numero2}")



def operacaoViaArgumento(argumentos):
    operar(argumentos[1:], 1)

def operacaoViaArquivo(nome_arquivo):
    args = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                linha = linha.replace("\n", "")
                args.append(linha)
        for i in range(len(args)):
            args[i] = args[i].split(" ")
            operar(args[i], i+1)
    else:
        print("Arquivo não encontrado!")

argumentos = sys.argv
nome_arquivo = argumentos[1]
if ".txt" not in nome_arquivo:
    operacaoViaArgumento(argumentos)
else:
    operacaoViaArquivo(nome_arquivo)
