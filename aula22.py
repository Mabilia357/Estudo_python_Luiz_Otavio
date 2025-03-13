# Operadores Lógicos
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser verdadeiras
# Se qualquer valor for considerado falso, ou verdadeiro,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que já vimos)
# 0, 0.0,  '' =  False
# Também existe o tipo None que é
# usado para representar um NAO valor

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'


#if entrada == 'E' and senha_digitada == senha_permitida:
#    print('Entar')
#else:
#    print('Sair')

#print(True and True and True) # exemplo de and, onde todas as opçoes são True, retorna True.

# Avaliação de curto circuito
#print(True and False and True) # nessa condição, o python analisa a função e ele sabendo que um False invalida,
# de avaliação de curto circuito.

# da mesma forma, como dito anteriormente, um valor 0, 0.0 ou uma string vazia, nos retorna como False.
#print(True and 0 and True)
#print(True and '' and True) aqui, alguns exemplos.

# abaixo o uso do 'or'

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'

# exemplo abaixo onde a condição verifica 'E' ou 'e', tbm é possível verificar a condição or e and da entrada primeiro,
# colocadno entre parenteses.

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entar')
#else:
#    print('Sair')

# Avaliação de curto-circuito

# no sistema de curto-cicuito em 'or', ele avalia a sentença True, ex:
#print(True or False) = True
#print(True or 0) # = True

#abaixo exemplo onde com uma linha só, verificamos a veracidade da expressão
#senha = input('Senha: ') or 'Sem senha'
#print(senha)