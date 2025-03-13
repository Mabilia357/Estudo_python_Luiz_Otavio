"""
split e join com list e str
split - divide uma string
join - une uma string
"""
#frase = '  Olha só que  S, coisa interessante'
#lista_frases = frase.split() # a função split divide uma frase por exemplo usando so espaços em branco, ou outros caracteres especificos.
#lista_frases = frase.split(',') # tbm é possivel informar onde queremos a divisão, nesse caso na virgula da frase.
#print(lista_frases)

# outra maneira de editar a frase é atraves do for.
# vamos aterar a frase na lista_frase, ou seja pegaremos o valor dela e alteraremos o proprio lista_frases,
# porque na string não é possivel, ela é imutável.

#for i, frase in enumerate(lista_frases):
    #lista_frases[i] = lista_frases[i].strip() # funçãoo strip, corta os espacos de inico e fim na frase alterada. rstrip() direita e lstrip() esquerda.

#print(lista_frases)

# Para adicionar itens na lista

frase = '  Olha só que  S, coisa interessante'

lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases_cruas.append(lista_frases_cruas[i].strip())
    
print(lista_frases_cruas)
print(lista_frases)

frases_unidas = '-'.join('abc')
print(frases_unidas)