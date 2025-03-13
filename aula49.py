"""
Listas em Python
Tipo list - mutável 
SUportta varios valores de qualuer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # o objeto append(), adiciona um item no ultimo indice de uma lista
lista.pop() # o objeto pop(), apaga o ultimo itetm adicionado em uma lista.
lista.append(60)
lista.append(70)
lista.pop()
del lista[2] # deleta o indice.
ultimo_item = lista.pop(1) # aqui um exemplo, pegando o item 1 do indice e colocando em uma variavel.
print(lista, 'Removido', ultimo_item)
lista.append(80) # adicioando no utlimo indice com o objeto append(), o valor de 80.
del lista[-1] # deletando o ultimo indice.
print(lista)