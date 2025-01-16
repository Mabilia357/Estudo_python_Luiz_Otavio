"""
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
abaixo temos um exemplo de uso, essas funcoes elas burlan os erros, a grosso modo, e criam uma execessão.
O exemplo abaixo é apenas instrutivo.
"""
numero_str = input('Vou dobrar o numero que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero')    