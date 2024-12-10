# Operadores in e not in, basicamente, in = está entre e not in = não esta entre
# Strings são iteráveis significa que podemos navegar item por item, como exemplo abaixo.
# 0 1 2 3 4 5
# O t á v i o
# -6 -5 -4 -3 -2 -1

# Abaixo exemplo de iterabilidade, é possivel navegar em uma string conforme exemplo.

nome = 'Otávio'
print(nome[2])
print(nome[-4])

# pelo fato de serem iteráveis é possivel trabalhar com as expressoes in e not
print('á' in nome) # retorna uma condição bool, True.
print('z' in nome) # tabém faz o contrário, verifica se o caracter 'z' está na variavel nome. aqui sendo falso.
print('vio' not in nome) # invertendo a expressão, a condição perguntta se 'vio' nao esta no nome e retorna false, porque está.
print('zero' not in nome) # aqui retorna um bool, True, porque ele pergunta, zero nao está no nome? sim é verdadeiro, ele não esta.

# um exemplo de uso simples

nome = input('Digite seu Nome: ')
encontrar = input('Digite o que deseja enconrtar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')