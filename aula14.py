a = 'A'
b = 'B'
c = 1.1
d = 1
string = 'a={nome2} b={nome1} a={nome1} c={nome3:.2f} d={nome4}'
formato = string.format(nome1=a, nome2=b, nome3=c, nome4=d) # parametro nomeado
# tambem é possivel argumentar por indice, em dev, se inicia em 0,1,2,3 e assim por diante.


print(formato)

# Outra opção para uso da função format.