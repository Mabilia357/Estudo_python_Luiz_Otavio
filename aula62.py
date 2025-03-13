"""
Operação ternaria (condicional de uma linha)
<valor> if <condicao> else <outrto valor>
"""
#condicao = 10 == 11
#variavel = 'valor' if condicao else 'outro valor'
#print(variavel)
# digito = 9 # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# print(novo_digito)
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

# Abaixo um outro exemplo de uso em uma linha só, nao recomendado.

print('Valor' if False else 'Outro valor' if False else 'Fim')