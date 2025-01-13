"""
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p][::]
Obs.: a função len retorna o qtd de caractteres str.
"""

variavel = 'Olá mundo'
print(variavel[4]) # exemplo de fatiamento de str, através do seu indice, no colchete indicamos o indice
# da str, seguindo o exemplo da variavel e os indicies da linha 3, 4 e 5.O uso de dois pontos,
# indicam que queremos uma fatia por exemplo: print(variavel[2:6]), aqui indica que quero pegar a fatia
# de inicio 2 até 6, da mesma forma quando omitimos, os indices antes e depois dos dois pontos,
# o python entende que o fatiamento começa no inicio nesse caso -> [:8] e vai até o indice 8 e ao
# contrario que -> [5:], indica ir do indice 5 até o final.

# uso da função len
variavel = 'Olá Mundo'
print(len(variavel))
# a funcção len, conta qtos indices a variavel possui, começando do 1, porque é contagem, não indice.
variavel = 'Olá Mundo'
print(len(variavel[3])) # aqui contamos qtos caracteres tem no indice 3. sendo igual a 1.
# outro exemplo de uso é o uso do [p], passo.
print(variavel[0:9:3]) # o ultimo numero o '3', indica que o passso será pular o indice de 3 em 3. apenas um exemplo.
# no passo, é possivel usar indice negativo, assim ele inverte o sentido da string.
print(variavel[-1:-10:-1]) # começa no -1 e vai até o -10, ou seja inverteu a str.
