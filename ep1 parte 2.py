# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:40:39 2018

@author: andre
"""

cardapio ={}

comanda = {}
 
print('''
   Comanda eletrônica
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
        comanda[produto]=0
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
        print(cardapio)
    elif n==5:
        produto=(input('Nome do produto:'))  
        if produto not in cardapio:
            print('O item {} não está no cardápio'.format(produto))
        else:
            while True:
                adicionar = int(input('Quantidade a adicionar:'))
                if adicionar<=0:
                    print('Não é possível adicionar quantidade não positiva')
                else:
                    comanda[produto]= comanda[produto] + adicionar 
                    print('Quantidade atual de {} na comanda :{}'.format(produto,comanda[produto]))
                    break
    elif n==6:
        produto=(input('Nome do produto:'))  
        if produto not in comanda:
            print('O item {} não está na comanda'.format(produto))
        else:
            while True:
                remover=int(input('Quantidade a remover:'))
                if remover<=0:
                        print('Não é possível remover quantidade não positiva') 
                elif remover > comanda[produto]:
                    print('Não é possível remover mais do que a quantidade presente na comanda')
                else:  
                    comanda[produto]=comanda[produto]- remover
                    print('Quantidade atual de {} na comanda :{}'.format(produto,comanda[produto]))
                    break
    elif n==7:
        print(comanda)
                    
print('Até mais')    