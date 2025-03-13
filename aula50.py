"""
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizaveis - indices e fatiamento
Métodos úteis:
    append - add um item ao final
    insert - add um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create  read   Update   Delete
Criar,  ler,  Alterar,  Apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear() limpar a lista
lista.insert(0, 5) # inserir algo na lista, nesse exemplo, no indice 0 o numero 5, pode ser qualquer dado.
print(lista)
print(lista[2]) # acessar um indice
#print(lista[6]) # nesse caso o python gera um erro de listt index out of range (nao existe)
lista.insert(100, 6) # nesse caso nosso ecxemplo nao possui o indice 100, mas o python poe o 6 no ultimo item do indice.
print(lista)