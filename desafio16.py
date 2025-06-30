#num = float(input('Digite um número : '))
#
#print(f'Onumero {num:.2f} tem a parte inteira {int(num)}')

from math import trunc

num = float(input('Digite um número : '))

print(f'O numero {num:.2f} tem a parte inteira {trunc(num)}')