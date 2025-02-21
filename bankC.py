def dep(valor):
    global saldo
    global trans
    
    saldo = saldo + valor
    trans.append(valor)
    
    
def sacar(valor):
    global saldo
    global trans
    
    valor = -valor
    saldo = saldo - valor
    trans.append(valor)
    
def extrato():
    for i in trans:
        print(i)
        
    print('Saldo final: {saldo}')
    
    
saldo = 0  
trans = []  


while True:
    op = input('Digite 1 para depositar; 2 para sacar; 3 para extrato; 0 para sair')
    
    if op == '1':
        valor = float(input('Digite o valor a ser depositado: '))
        dep(valor)
        
    elif op == '2':
        valor = float(input('Digite o valor a ser sacado: '))
        sacar(valor)
        
    elif op == '3':
        extrato()
        
    elif op == '0':
        break