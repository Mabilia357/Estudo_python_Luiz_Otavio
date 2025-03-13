"""
Enumerate - enumera iteráveis (indices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João)]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
print(lista)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])