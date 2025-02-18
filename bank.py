# Variáveis globais
contas = {}
saldo_total = 0
extratos = {}

def criar_conta(numero, saldo_inicial):

    global contas
    if numero not in contas:
        contas[numero] = saldo_inicial
        extratos[numero] = []
        print(f"Conta {numero} criada com saldo {saldo_inicial}")
    else:
        print(f"Conta {numero} já existe")

def depositar(numero, valor):
    global contas
    if numero in contas:
        contas[numero] += valor
        extratos[numero].append(f"Depósito: +{valor}")
        print(f"Depósito de {valor} realizado na conta {numero}")
    else:
        print(f"Conta {numero} não existe")

def sacar(numero, valor):
 
    global contas
    if numero in contas:
        if contas[numero] >= valor:
            contas[numero] -= valor
            extratos[numero].append(f"Saque: -{valor}")
            print(f"Saque de {valor} realizado na conta {numero}")
        else:
            print(f"Saldo insuficiente na conta {numero}")
    else:
        print(f"Conta {numero} não existe")

def verificar_saldo(numero):

    global contas
    if numero in contas:
        print(f"Saldo da conta {numero}: {contas[numero]}")
    else:
        print(f"Conta {numero} não existe")

def gerar_extrato(numero):

    global extratos
    if numero in extratos:
        print(f"Extrato da conta {numero}:")
        for item in extratos[numero]:
            print(item)
    else:
        print(f"Conta {numero} não existe")

criar_conta(123, 1000)
depositar(123, 500)
sacar(123, 200)
verificar_saldo(123)
gerar_extrato(123)