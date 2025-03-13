"""
iterável -> str, range, etc
Itterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""
# O que acontece em um laço for

texto = 'Luiz' # iterável
# iterador = iter(texto) # iterador

# while True:
#   try:
#       letra = next(iterador)
#       print(letra)
#   except StopIteration:
#       break

for letra in texto:
    print(letra)