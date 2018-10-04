
cardapio ={}

comanda = {}
 
print('''
   Menu
      0 – sair
      1 – adicionar item no cardapio
      2 – remover item no cardapio
      3 – alterar preço 
      4 – imprimir cardápio
      5 – adicionar item na comanda
      6 – remover item na comanda
      7 – imprimir comanda''')
while True:
   
    n=int(input('Faça sua escolha:'))
    if n <0 or n >7:
        print('numero invalido')
    elif n==0:
        break 
    elif n==1:
        produto=(input('Nome do produto:'))
        preco= float(input('preço do produto:'))
        cardapio[produto]=preco
    elif n==2:
        produto=(input('Nome do produto:'))
        if produto not in cardapio:
            print('O item {} não está no cardapio'.format(produto))
        else:    
            del cardapio[produto]
    elif n==3:
        produto=input('produto que deseja alterar:')
        if produto not in cardapio:
            print('O item {} não está no cardapio'.format(produto))
        else:    
            preco= float(input('Novo preço:'))
            cardapio[produto]=preco
        
    elif n==4:
        if cardapio=={}:
            print('cardapio vazio')
        else:    
            for produto in cardapio:
                print(produto,cardapio[produto])
        
    elif n==5:
        add_comanda=input('quer adicionar uma comanda?(s/n)')
        if add_comanda in 'Ss':
            numero_comanda=int(input('numero da comanda:'))
            comanda_n={}
            comanda_n[produto]=0
        produto=(input('Nome do produto:'))  
        if produto not in cardapio:
            print('O item {} não está no cardápio'.format(produto))
        else:
            while True:
                adicionar = int(input('Quantidade a adicionar:'))
                if adicionar<=0:
                    print('Não é possível adicionar quantidade não positiva')
                else:
                    
                    comanda_n[produto]= comanda_n[produto] + adicionar
                    print('Quantidade atual de {} na comanda :{}'.format(produto,comanda_n[produto]))
                    break
    elif n==6:
        produto=(input('Nome do produto:'))  
        if produto not in comanda_n:
            print('O item {} não está na comanda'.format(produto))
        else:
            while True:
                remover=int(input('Quantidade a remover:'))
                if remover<=0:
                        print('Não é possível remover quantidade não positiva') 
                elif remover > comanda_n[produto]:
                    print('Não é possível remover mais do que a quantidade presente na comanda')
                else:  
                    comanda_n[produto]=comanda_n[produto]- remover
                    print('Quantidade atual de {} na comanda :{}'.format(produto,comanda_n[produto]))
                    break
    elif n==7:
        if comanda_n=={}:
            print('comanda vazia')
            valor_total=0
        else:
            valor_total=0
            for produto in comanda_n:
                preco=cardapio[produto]
                quantidade=comanda_n[produto]
                valor_total+=preco*quantidade
                print('{} - preço unitário :{}'.format(produto,preco))
                print('quantidade de {} - {}'.format(produto,quantidade))
                print('preço total de {}: {}'.format(produto,preco*quantidade))
            print('Total:{}'.format(valor_total))
            print('Total (com 10%) : {}'.format(valor_total*1.1))
    comanda['comanda', numero_comanda]=comanda_n       
          
print('Até mais,volte sempre')    