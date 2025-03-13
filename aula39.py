"""
Repetiçoes
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Looop infinito -> Quando um codigo não tem fim.
"""
# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
    
#     linha += 1
    
    
# print('acabou')    
"""
Iterando strings com while
"""
nome = 'Gustavo'
tamanho_nome = len(nome)
print(tamanho_nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    
novo_nome += '*'
print(novo_nome)

# exercicio iterando strings, e adicionando caractteres em um nome ou variavel já definida.