"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permitta que o programa quebre com erros
de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('Selecione uma opção: [i]nserir, [a]pagar, [l]istar: ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar')
            
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i , a ou l.')