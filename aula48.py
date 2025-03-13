"""
Listas em Python
Tipo de list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentto reutilizável - indices e fatiamento
Métodos úteis: append, insertt, pop, del, clear, extend, +
"""
#        -54321
#        +01234
string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) # falsy string vazia
# print(lista, type(lista))

#        0     1       2            3      4
#       -5    -4      -3           -2     -1
lista = [123, True, 'Luiz Otávio', 1.2,   []] # a lista é composta por itens conforme exemplo acima 
lista[-3] = 'Maria' # é possivel alterar um elemento dentro da lista, atraves de [] e seu indice, tanto negativo como positivo
print(lista)
print(lista[2], type(lista[2]))