n = int(input('Digite um número para saber seu fatorial : '))
c = n
f  =1
print(f'Calculando {n}! = ', end='')
while c > 0 :
  print(f'{c}', end= ' ')
  print(' X ' if c > 1 else ' = ', end='')
  f *= c
  c -= 1
print(f'{f}')

#minha solução
# numero = int(input('Informe um número para calcular seu fatorial : '))
# contador = 1
# total = 1
# print(f'Fatorial de {numero}! = {numero} X', end=' ')
# while contador != numero:
#     total *= numero
#     numero -= 1
#     print(f'{numero} X ', end= '')
# print(f' = {total}')

#solução simples professor
#from match import factorial
#
#n = int(input('Digite um número para calcular seu fatorial : ')
#f = factorial(n)
#print(f'O fatorial de {n} é {f}')

#outra solução
