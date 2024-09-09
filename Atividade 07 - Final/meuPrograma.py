import sys
import os

def operar(argumentos, id):
    # Encontrar a operação
    operacoes = {"+", "-", "*", "/"}
    operacao = next((arg for arg in argumentos if arg in operacoes), None)

    # Encontrar os números
    numeros = [int(arg) for arg in argumentos if arg.isdigit()]

    if operacao is None or len(numeros) < 2:
        print("Argumentos inválidos!")
        return

    numero1, numero2 = numeros[:2]

    # Realizar a operação
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: Divisão por zero!")
            return
        resultado = numero1 / numero2

    print(f"Resultado da operação {id}: {resultado}")




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
if len(argumentos) < 2:
    print("Argumentos insuficientes!")
    sys.exit()
nome_arquivo = argumentos[1]
if ".txt" not in nome_arquivo:
    operacaoViaArgumento(argumentos)
else:
    operacaoViaArquivo(nome_arquivo)
