t = int(input('Digite um número para ver sua tabuada : '))

for c in range (0, 11):
    r = t * c
    print(f'[{t}] x [{c}] = {r}')


# solução simplificada

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'[{num}] x [{c}] = [{num * c}]')
