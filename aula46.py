for i in range(10): # item por item do range(10) de 0 a 9.
    if i == 2: # se  i for 2, imprima (print) e continua..
        print('i é 2, pulano...')
        continue
    
    if i == 8: # a medida que for 8, (print),  e quebra no break. sem execução do else.
        print('i é 8, seu else não executará')
        break
    
    for j in range(1, 3): # inicie do 1 ate o 3, sendo o J a coluna por assim dizer
        print(i, j)
else:
    print('For completo com sucesso!')