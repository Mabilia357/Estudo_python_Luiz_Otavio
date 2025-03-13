"""Exemplo comun de uso while"""

# senha_salva = '1223456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    
#     repeticoes += 1
    
# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

""" Exemplo de Laço For """

texto = 'Python'

novo_texto = ''
for letra in texto: # para cada letra in texto iterável qye é = 'Python', exiba letra.
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
    
