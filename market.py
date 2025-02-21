def adicionar_produto(produtos):
    global cart
    cart.append(produtos)

def remover_produto(produtos):
    global cart

    for i in range(len(cart)):
        if cart[i] == produtos:
            cart.pop(i)
            break
def ver_produto(produtos):
    for i in cart:
        print(i)
    
cart = []

while True:
    op = input('Digite 1 para adicionar produto; 2 para remover produto; 3 para ver produtos; 0 para sair')
    
    if op == '1':
        produto = input('Digite o produto a ser adicionado: ')
        adicionar_produto(produto)
        
    elif op == '2':
        produto = input('Digite o produto a ser removido: ')
        remover_produto(produto)
        
    elif op == '3':
        ver_produto()
        
    elif op == '0':
        break
    
for i in cart:
    print(i)
    
for i in range(len(cart)):
    print(i)
    print(cart[i])
    
carrinho = ['a', 'b', 'c' ,'d']