# calculo manual

# hipot = (adj**2 + op**2)**(1/2)

from math import hypot

adj = float(input('Informe o comprimento do cateto adjacente : '))
op = float(input('Informe o comprimento do cateto oposto : '))

hipot = hypot(adj, op)

print(f'O comprimento da hipotenusa é {hipot:.2f}')





