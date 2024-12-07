# \r\n -> CRLF -> Carriage Return Line Feed (padrao windows)
# \n -> LF -> padrao linux, unix e mac
print(12, 34, 1011, sep="-", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
# sep -> significa definição de separador, quer pode ser definido em aspas simples ou duplas.
# end -> define o tipo de quebra de linha, por padrão windows, usamos o CRLF, sendo assim não é necessário definir, se for usar o LF,
# padrao Unix ou Mac, devemos usar o comando end='\n'.

# Observação, se tivermos o comando print vazio, print(), ele estará cumprindo o padrão CRLF,
# que determina a quebra de linha. Verifique o exemplo abaixo.

print()
print()
print()

# Ao executar o codigo print() vazio, teremos linhas em branco.