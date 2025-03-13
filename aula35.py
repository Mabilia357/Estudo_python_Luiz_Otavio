"""
Repetiçoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Looop infinito -> Quando um codigo não tem fim.
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair': 
        break # esse comando, vai até o while mais proximo dele, e acima ele só acaba com a digittação de break.
    
print('Acabou')

# exemplos de while.