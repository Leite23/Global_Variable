import time

contas = {}
extratos = {}

def criar_conta(numero, saldo_inicial):
    if numero not in contas:
        contas[numero] = saldo_inicial
        extratos[numero] = []
        print(f"Conta {numero} criada com saldo {saldo_inicial}")
    else:
        print(f"Conta {numero} já existe")

def depositar(numero, valor):
    if numero in contas:
        contas[numero] += valor
        extratos[numero].append(f"Depósito: +{valor}")
        print(f"Depósito de {valor} realizado na conta {numero}")
    else:
        print(f"Conta {numero} não existe")

def sacar(numero, valor):
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
    if numero in contas:
        print(f"Saldo da conta {numero}: {contas[numero]}")
    else:
        print(f"Conta {numero} não existe")

def gerar_extrato(numero):
    if numero in extratos:
        print(f"Extrato da conta {numero}:")
        for item in extratos[numero]:
            print(item)
    else:
        print(f"Conta {numero} não existe")

def menu():
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Verificar saldo")
    print("5. Gerar extrato")
    print("6. Sair")

def main():
    while True:
        menu()
        opcao = input("Digite a opção: ")
        if opcao == "1":
            numero = int(input("Digite o número da conta: "))
            saldo_inicial = float(input("Digite o saldo inicial: "))
            criar_conta(numero, saldo_inicial)
        elif opcao == "2":
            numero = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a depositar: "))
            depositar(numero, valor)
        elif opcao == "3":
            numero = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a sacar: "))
            sacar(numero, valor)
        elif opcao == "4":
            numero = int(input("Digite o número da conta: "))
            verificar_saldo(numero)
        elif opcao == "5":
            numero = int(input("Digite o número da conta: "))
            gerar_extrato(numero)
        elif opcao == "6":
            print("Encerrando o programa...")
            time.sleep(10)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()