"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) x gera hexadecimal minusculo e p X um hexadecimal maiusculo.
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco) # exemplo de interpolação, formatação de strings.
print(variavel)

print('O hexadecimal de %d é %0.4x' % (15, 15)) # exemplo de interpolação com numeros hexadecimais.