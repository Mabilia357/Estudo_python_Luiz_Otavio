"""
Tipo tupla - Uma lista imutável
"""
nomes = ['Maria', 'Helena', 'Luiz']
print(nomes)

# cirar uma tupla: nomes = 'Maria', 'Helena', 'Luiz' a tupla é uma lista sem colchetes
# a tupla não pode ser mutável, podemos alterar ela coergindo ela para tipo list(), e apos isso 
# transformar para uma tupla.

nomes = 'Maria', 'Helena', 'luiz'
print(nomes)

# a tupla pode ser criarda tbm apenas com parenteses

nomes = ('Maria', 'Helena', 'Luiz')
print(type(nomes))


# lembrando novamente, são imutáveis.