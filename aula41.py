""" while/else"""
string = 'valor qualquer'

i = 0 # variavel i refere-se a um indice comun para contar (index)
while i < len(string): # checando se o indice i é menor que o tamanho da string no caso a função len.
    letra = string[i] # avaliando indice por indice, pegando letra por letra
    
    if letra == ' ': # ex: procurar um espaço em branco numa str.
        break # nesse formato um break não executa o else, se tiver um break dentro de um while, nao executa o while
    
    print(letra) # imprimindo letra por letra na tela
    i += 1 # aqui pegando letra por letra e adicionando mais um indice
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')