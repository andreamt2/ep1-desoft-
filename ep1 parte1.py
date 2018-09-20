# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:37:53 2018

@author: andre
"""
lista_vazia= {}

cardapio ={}

comanda = {}
 
print('''
   Comanda eletrônica
      0 – sair
      1 – imprimir cardápio
      2 - adicionar item
      3 - remover item
      4 - imprimir comanda''')
while True:
    n=int(input('Faça sua escolha:'))
    if n <0 or n >4:
        print('numero invalido')
    elif n==0:
        break 
    elif n==1:
        print(cardapio)
    elif n==2:
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
                    print('Quantidade atual de {}:{}'.format(produto,comanda[produto]))
                    break
    elif n==3:
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
                    print('Quantidade atual de {}:{}'.format(produto,comanda[produto]))
                    break
    elif n==4:
        print(comanda)
                    
            
   
print('Até mais')    
    
