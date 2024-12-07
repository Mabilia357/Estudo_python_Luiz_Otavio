# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primtivos:
# str, int, float, bool
print(int('1'), type(int('1'))) # neste exemplo temos a coerção de uma str em int.
print(float('1') + 1) # nesse caso a coerção de str para float, tras um resulato float, pelo uso do ponto.
print(type(float('1') + 1)) # executa de dentro para fora e mostra o ultimo passo da classe que é o type, tipo.
print(bool(' ')) # boolean, uma função vazia é False, uma função em branco, ou com um espaço vazio, é True.
print(str(11) + 'b') # tbm é possivel a coerção de um dado int em str, e o resultado uma concatenação.
print(int('1') + int('1')) # aqui uma str em um dado int.
# O python é uma linguagem forte e dinamica, isso significa que algumas coisas não são possiveis coagir
#print(int(B) + 1) # como esse exemplo.
