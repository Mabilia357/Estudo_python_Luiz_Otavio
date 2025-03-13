""" Calculadora com while """
while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador desejado (+-/*): ')
    
    numeros_validos = None  # flag
    num_1_float = 0
    num_2_floal = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_floal = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos numeros digitados são invalidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador Inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. confira o resultado abaixo: ')
    
    if operador == '+':
        print(f'{num_1_float}+{num_2_floal} =', num_1_float + num_2_floal)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_floal} =', num_1_float - num_2_floal)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_floal} =', num_1_float / num_2_floal)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_floal} =', num_1_float * num_2_floal)
    else:
        print('Nunca deveria ter chegado aqui')    
    
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s') # minusculo e str, starswith, inicia com e bool.
    
    if sair is True:
        break