lista = []
par = []
impar = []

while True:
    numero = int(input('Digite um valor : '))
    lista.append(numero)
    if numero % 2 == 0 :
        par.append(numero)
    else:
        impar.append(numero)
    continuar = input('Deseja continuar ? [S/N] : ').strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'A lista coompleta é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

# solução professor
'''
num = []
par = []
impar = []

while True:
    num.append(int(input('Digite um número : )))
    resp = str(input()'Deseja continuar ? [S/N])
    if resp in 'Nn':
        break
for i, v in enumerate(num)
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
        
print(f'A lista coompleta é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
'''