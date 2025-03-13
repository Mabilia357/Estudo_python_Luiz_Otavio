#frase = 'O Python é uma linguagem multiparadigma e o criador foi ' \
#'Guido Von Rossum .' \
    

# i = 0

# while i < len(frase):
#     letra_atual = frase[i]
    
#     print(letra_atual)
#     i += 1

# for caractere in frase:
#     print(caractere)

# lista = [1, 2, 3, 4, 5]
# tamanho = len(lista)
# print(tamanho)

# start = 0
# end = 10
# while start < end:
#     start += 1
#     print(start)

linhas = 2
colunas = 2

linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1