# Operadores Lógicos
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser verdadeiras
# Se qualquer valor for considerado falso,
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