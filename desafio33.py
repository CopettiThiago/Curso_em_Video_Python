n1 = int(input('Digite o primeiro numero : '))
n2 = int(input('Digite o segundo numero : '))
n3 = int(input('Digite o terceiro numero : '))

if n1 > n2 and n1 > n3:
    print(f'O maior numero é {n1}')
    if n2 > n3:
        print(f'O menor numero é {n3}')
    else:
        print(f'O menor numero é {n2}')
elif n2 > n1 and n2 > n3:
    print(f'O maior numero é {n2}')
    if n1 > n3:
        print(f'O menor numero é {n3}')
    else:
        print(f'O menor numero é {n1}')
else:
    print(f'O maior numero é {n3}')
    if n1 > n2:
        print(f'O menor numero é {n2}')
    else:
        print(f'O menor numero é {n1}')

# outra solução
'''
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n2
if n1 > maior:
    maior = n1
if n3 > maior:
    maior = n3
print(f'O maior numero é {maior} e o menor numero é {menor}')
'''
