"""
Flag (Bandeira) - Marcar um local, declarar uma variavel durante um blco de codigos, não ´´e uma
boa pratica, mas se usarmos a tecnica Flag, onde colocamos uma bandeira, destacando onde o codigo esta.
None = Não valor, atribuição sem valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""



condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
    
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
