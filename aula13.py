nome = 'Gustavo Mabilia'
altura = 1.74
peso = 87.5
imc = peso / (altura * altura ) # ou peso / altura ** 2.
#print(nome, 'tem', altura, 'metros de altura, pesa', peso, 'quilos e seu IMC é de:',imc )

"f-strings" # introdução sobre formatação de strings.

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Gustavo mabilia tem 1.74 de altura, pesa
# 87.5 quilos e seu IMC é de: 
# Formula => IMC = peso / (altura x altura)