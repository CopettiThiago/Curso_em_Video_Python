numeros = []
maior = maior = 0
for c in range(0,5):
    numeros.append(int(input(f'Digite um número para a posição {c} :')))
    if c == 0:
        maior = menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]

print('=-' * 30)
print(f'Os números digitados foram {numeros}')
print(f'O maior número digitado foi {maior} na posição ', end='')
for i, n in enumerate(numeros):
    if n == maior:
        print(f'{i}...', end= '')
print()
print(f'O menor número digitado foi {menor} na posição ', end= '')
for i, n in enumerate(numeros):
    if n == menor:
        print(f'{i}...', end='')
        