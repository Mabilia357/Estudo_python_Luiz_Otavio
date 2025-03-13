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

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a + lista_b # concatena, ou seja junta.
print(lista_c)
lista_a.extend(lista_b) # retorna None
print(lista_a)