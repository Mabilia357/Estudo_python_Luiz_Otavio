"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é par ou ímpar. caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""
# numero = input('Digite um número inteiro: ')

# try:
#     int_numero = int(numero)
    
#     if int_numero % 2 == 0:
#         print(f'{int_numero} é um numero par!')
#     else:
#         print('f{int_numero}, é um numero ímpar!')
# except ValueError:
#     print('Isso não é um numero inteiro, digite novamente.')

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação aprorpiada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Digite a hora atual: ')

# hora_atual = float(hora)

# if 0 <= hora_atual <= 11:
#     print('Bom dia')
# elif 12 <= hora_atual <= 17:
#     print('Boa Tarde')
# elif 18 <= hora_atual <=23:
#     print('Boa Noite')
# else:
#     print('Digite uma hora válida!')

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se ttiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Escreva somente seu primeiro nome: ')


if nome == (nome[0:4]):
    print('Seu nome é curto')
elif nome == (nome[0:6]):
    print('Seu nome é normal')
else:
    print('Seu nome é grande!')
