"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://em.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.htm
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2 # exemplo da imprecisão
print(numero_3)
print(f'{numero_3:.2f}') # ajustando valor, mas em str, ou seja nao manttemos o valor float.
# uma maneira de resolver isso é atraveds da função round().
print(round(numero_3, 2)) # ele arredonda, então é importante sinlaizar qtas casas depois da virgula
# é importante, conforme o exempolo do pirnit acima.

#ourta maneira é atraves da import decimal, usado em casos de extrema precisõa, vide exemplo.

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)

# Obs. ao usar o import decimal, devemos usar conforme o exemplo acima, ou seja, em calculo float,
# devemos converter para string.